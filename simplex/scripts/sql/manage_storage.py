import os
import argparse
from pathlib import Path
from simplex.infrastructure.storage.management.storage_management_api import (
    SimplexStorageManagementAPI
)

ROOT = os.path.realpath(os.path.expanduser(__file__))


def apply_patches(api):
    patchdir = Path(ROOT).parents[3]
    patchdir = patchdir / 'resources/sql/quickstart'
    for patch in patchdir.iterdir():
        api.apply_patch_sql(patch)


def main():
    parser = argparse.ArgumentParser(
        description='Manage Simplex storage and schemata.')
    parser.add_argument(
        '--force',
        '-f',
        type=str,
        help='Do not prompt before performing dangerous operations.')
    parser.add_argument(
        '--hostname',
        type=str,
        help='Operate on the database server identified.')
    parser.add_argument(
        '--port',
        type=str,
        help='Port on which the database is listening.')
    parser.add_argument(
        '--username',
        '-u',
        type=str,
        help='Connect with the specified username.'
    )
    parser.add_argument(
        '--password',
        '-p',
        type=str,
        help='Connect with the specified password.'
    )
    parser.add_argument(
        '--namespace',
        type=str,
        help='Connect with the namespace.'
    )

    args = parser.parse_args()

    api = (
        SimplexStorageManagementAPI()
        .set_host(args.hostname)
        .set_user(args.username)
        .set_password(args.password)
        .set_port(args.port)
        .set_namespace(args.namespace))

    apply_patches(api)


if __name__ == '__main__':
    main()
