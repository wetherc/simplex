#!/usr/bin/env python3

import argparse
from simplex import Env, SimplexManagement


def unflatten_input(input):
    resultDict = dict()
    for key, value in input.items():
        parts = key.split('.')
        _d = resultDict
        for part in parts[:-1]:
            if part not in _d:
                _d[part] = dict()
            _d = _d[part]
        _d[parts[-1]] = value
    return resultDict


def main():
    parser = argparse.ArgumentParser(
        description='Manage Simplex configurations.',
        prog='base')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--list',
        action='store_true',
        help='./bin/config --list')
    group.add_argument(
        '--get',
        action='append',
        help='./bin/config --get key')
    group.add_argument(
        '--set',
        action='append',
        nargs=2,
        help='./bin/config --set key value')
    group.add_argument(
        '--delete',
        action='append',
        help='./bin/config --delete key')
    args = parser.parse_args()

    workflow = SimplexManagement.SimplexManagementWorkflow()
    config_source = Env.SimplexConfig.SimplexConfigLocalSource()

    if args.set is not None:
        _config_vals = dict((elem[0], elem[1]) for elem in args.set)
        _config_vals = unflatten_input(_config_vals)

        config_source.set_keys(_config_vals)
        config_source.save_config()

        workflow.log_info('Set local configuration values for {}'.format(
            ', '.join(_config_vals.keys())))

    if args.get is not None:
        _config_vals = [
            f'\n\t{key}:\t{config_source.get_key(key)}'
            for key in args.get
        ]
        workflow.log_info(''.join(_config_vals))

    if args.delete is not None:
        config_source.delete_keys(args.delete)
        config_source.save_config()

        workflow.log_info(f'Successfully deleted keys: {args.delete}')

    if args.list:
        _config_vals = [
            f'\n\t{key}:\t{val}'
            for key, val in config_source.config.items()
        ]

        workflow.log_info(''.join(_config_vals))


if __name__ == '__main__':
    main()
