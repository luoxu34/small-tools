#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: multi_host_run.py
Version: 0.3
Author: luoxu34
Summary: A small tool for publicSDK to filter related logs on multiple hosts.
Requires: fabric, compatible with fabric 1.x & 2.x
"""

import argparse

fb_version = ''
try:
    import fabric

    if hasattr(fabric, '__version__'):
        # fabric 2.x
        fb_version = fabric.__version__
    else:
        # fabric 1.x
        from fabric import version

        fb_version = version.__version__
except ImportError as e:
    print('[ERROR]Please install fabric first: pip install fabric')
    exit(-1)

if fb_version.startswith('1.'):
    from v1 import main
elif fb_version.startswith('2.'):
    from v2 import main
else:
    print('[SORRY] No support fabric version: {}'.format(fb_version))
    exit(-1)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Execute commands on multiple hosts.')
    parser.add_argument('cmd', help='the command that will be executed')
    parser.add_argument('--path', '-p', help='specify a path for remote hosts')

    args = parser.parse_args()

    # test: ./multi_host_run.py pwd -p /tmp
    main(args.cmd, args.path)

