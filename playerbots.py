#!/usr/bin/env python3
"""Choose, fetch and install a pinned ArcheAge PlayerBots component."""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def run(*args, cwd=None):
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        raise ValueError((result.stderr or result.stdout).strip() or f'{args[0]} failed')
    return result.stdout.strip()


def inside(value):
    if not isinstance(value, str) or not value or any(c in value for c in '\\:\x00'):
        raise ValueError('Invalid component path.')
    relative = PurePosixPath(value)
    if relative.is_absolute() or any(p in ('', '.', '..') for p in value.split('/')):
        raise ValueError('Invalid component path.')
    path = ROOT.joinpath(*relative.parts).resolve()
    if path == ROOT or not path.is_relative_to(ROOT):
        raise ValueError('Component path escapes the workspace.')
    return path


def catalog():
    entries = json.loads((ROOT / 'components.json').read_text(encoding='utf-8'))['components']
    result = {}
    paths = set()
    for entry in entries:
        key = entry['id']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', key) or key in result:
            raise ValueError('Invalid or duplicate component ID.')
        path = inside(entry['path'])
        if path in paths:
            raise ValueError('Duplicate component path.')
        inside(entry['guide'])
        if not re.fullmatch(r'https://github.com/NulightJens/ArcheAge-PlayerBots-[A-Za-z0-9-]+', entry['repository']):
            raise ValueError('Unexpected component repository.')
        result[key] = entry
        paths.add(path)
    return result


def git(*args, cwd=None):
    return run('git', '-C', str(ROOT if cwd is None else cwd), *args)


def pin(entry):
    # Gitlinks are the single revision lock; there is no second SHA list to drift.
    if git('diff', 'HEAD', '--', '.gitmodules', 'components.json', entry['path']):
        raise ValueError('Workspace selection has local changes. Preserve them and use a fresh clone.')
    fields = git('ls-tree', 'HEAD', '--', entry['path']).split()
    if len(fields) != 4 or fields[0:2] != ['160000', 'commit'] or fields[3] != entry['path']:
        raise ValueError('Missing revision lock. Clone the master with Git; ZIP downloads omit components.')
    return fields[2]


def state(entry):
    expected = pin(entry)
    path = inside(entry['path'])
    if not (path / '.git').exists():
        if path.exists() and any(path.iterdir()):
            raise ValueError(f'{entry["id"]}: existing non-repository directory; preserve it and use a fresh clone.')
        return 'not fetched', expected
    if Path(git('rev-parse', '--show-toplevel', cwd=path)).resolve() != path:
        raise ValueError(f'{entry["id"]}: incorrect repository root.')
    actual = git('rev-parse', 'HEAD', cwd=path)
    if actual != expected:
        raise ValueError(f'{entry["id"]}: revision differs from the master pin; preserve this checkout and use a fresh clone.')
    if git('status', '--porcelain', '--untracked-files=all', cwd=path):
        raise ValueError(f'{entry["id"]}: local changes found; preserve them and use a fresh clone.')
    origin = git('remote', 'get-url', 'origin', cwd=path).removesuffix('.git')
    if origin != entry['repository']:
        raise ValueError(f'{entry["id"]}: origin differs from the catalog.')
    nested = git('submodule', 'status', '--recursive', cwd=path)
    if any(line.startswith(('+', 'U')) for line in nested.splitlines()):
        raise ValueError(f'{entry["id"]}: a dependency differs from its pin.')
    return ('dependencies missing' if any(line.startswith('-') for line in nested.splitlines()) else 'ready'), expected


def ready(entry):
    status, _ = state(entry)
    if status != 'ready':
        raise ValueError(f'Run: python playerbots.py fetch {entry["id"]}')
    return inside(entry['path'])


def fetch_source(entry):
    key = f'submodule.{entry["id"]}.url'
    urls = [git('config', '-f', '.gitmodules', '--get', key)]
    # Local submodule URLs can override .gitmodules even in a clean checkout.
    urls.extend(line.split('=', 1)[1] for line in git('config', '--local', '--list').splitlines()
                if line.startswith(key + '='))
    if any(url.removesuffix('.git') != entry['repository'] for url in urls):
        raise ValueError(f'{entry["id"]}: submodule URL differs from the catalog.')


def host_spec(entry):
    source = ready(entry)
    if entry['kind'] != 'variant':
        raise ValueError('This component has no standalone host installer. Use its guide.')
    manifest_name = 'overlay.json' if entry['id'].startswith('legacy') else 'playerbots.module.json'
    manifest = json.loads((source / manifest_name).read_text(encoding='utf-8-sig'))
    if manifest_name == 'overlay.json':
        host = {'repository': 'https://github.com/AAEmu/AAEmu', 'testedBaseCommit': manifest['hostCommit']}
    else:
        host = manifest['host']
    if host['repository'] not in ('https://github.com/AAEmu/AAEmu', 'https://github.com/NL0bP/AAEmu'):
        raise ValueError('Unexpected host repository.')
    if not re.fullmatch(r'[0-9a-f]{40}', host['testedBaseCommit']):
        raise ValueError('Invalid host revision.')
    return source, host


def outside(value):
    path = value.resolve()
    if path == ROOT or path.is_relative_to(ROOT) or ROOT.is_relative_to(path):
        raise ValueError('Choose a separate directory outside the master workspace.')
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog='Start with: python playerbots.py list')
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('list', help='Compare components and their intended use')
    commands.add_parser('status', help='Check local component revisions without changing them')
    commands.add_parser('doctor', help='Check Git, Python and .NET prerequisites')
    fetch = commands.add_parser('fetch', help='Download only a selected component and its dependencies')
    fetch.add_argument('component', nargs='?', help='Default: core')
    fetch.add_argument('--all', action='store_true', help='Download every pinned component')
    guide = commands.add_parser('guide', help='Show setup and commands for one component')
    guide.add_argument('component', nargs='?', default='core')
    host = commands.add_parser('prepare-host', help='Clone a new host at the selected variant\'s exact revision')
    host.add_argument('component', nargs='?', default='core')
    host.add_argument('--destination', type=Path, required=True, help='New directory outside this workspace')
    install = commands.add_parser('install', help='Run the selected variant\'s checked source installer')
    install.add_argument('component', nargs='?', default='core')
    install.add_argument('--host', type=Path, required=True, help='Separate clean host checkout')
    install.add_argument('--check', action='store_true', help='Validate without installing')
    args = parser.parse_args()
    try:
        entries = catalog()
        if args.command == 'list':
            for entry in entries.values():
                print(f'{entry["id"]:22} {entry["role"]}\n  {entry["summary"]}')
            print('\nRecommended: core. Use guide <component> for commands and limitations.')
        elif args.command == 'doctor':
            print(f'Python {sys.version.split()[0]}: {sys.executable}')
            if sys.version_info < (3, 11):
                raise ValueError('Python 3.11 or newer is required.')
            print(run('git', '--version'))
            sdks = run('dotnet', '--list-sdks')
            if not any(line.startswith('10.') for line in sdks.splitlines()):
                raise ValueError('.NET 10 SDK is required for the native source builds.')
            print('.NET 10 SDK available. Server data, database and matching client are configured separately.')
        elif args.command == 'status':
            failed = False
            for entry in entries.values():
                try:
                    status, revision = state(entry)
                    print(f'{entry["id"]:22} {status:22} {revision[:12]}')
                except ValueError as error:
                    print(str(error))
                    failed = True
            return int(failed)
        else:
            if args.command == 'fetch' and args.all and args.component:
                raise ValueError('Choose one component or --all.')
            key = args.component or 'core'
            if key not in entries:
                raise ValueError(f'Unknown component: {key}. Use list to see available names.')
            entry = entries[key]
            if args.command == 'guide':
                print(inside(entry['guide']).read_text(encoding='utf-8'))
            elif args.command == 'fetch':
                selected = list(entries.values()) if args.all else [entry]
                for item in selected:
                    state(item)
                    fetch_source(item)
                for item in selected:
                    path = item['path']
                    print(f'Fetching {item["id"]}...', flush=True)
                    git('submodule', 'update', '--init', '--recursive', '--checkout', '--', path)
                    ready(item)
                    print(f'Ready: {item["id"]}')
            elif args.command == 'prepare-host':
                _, spec = host_spec(entry)
                destination = outside(args.destination)
                if destination.exists() or destination.is_symlink():
                    raise ValueError('Host destination already exists; choose a new directory.')
                print(f'Preparing {entry["id"]} host in {destination}...', flush=True)
                run('git', 'clone', '--filter=blob:none', '--no-checkout', spec['repository'], str(destination))
                git('checkout', '--detach', spec['testedBaseCommit'], cwd=destination)
                print(f'Host ready at {spec["testedBaseCommit"]}. Run install with --check next.')
            elif args.command == 'install':
                source, _ = host_spec(entry)
                host_path = outside(args.host)
                command = [sys.executable, '-B', str(source / 'install.py'), '--host', str(host_path)]
                if args.check:
                    command.append('--check')
                print(run(*command, cwd=source))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'PlayerBots: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
