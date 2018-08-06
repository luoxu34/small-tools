#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric2 import SerialGroup

from base import print_result, HOSTS, LOG_PATH


def cd_and_run(c, cmd, path=None):
    if not cmd:
        return ''

    if path:
        cmd = 'cd {} && {}'.format(path, cmd)
    result = c.run(cmd, hide=True)
    return result.stdout or result.stderr


def main(cmd, path=LOG_PATH):
    for cxn in SerialGroup(*HOSTS):
        print_result(cxn.host, cd_and_run(cxn, cmd, path))


if __name__ == '__main__':
    main('pwd')
