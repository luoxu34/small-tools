#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: multi_host_run
Version: 0.2
Author: luoxu34
Summary: A small tool for publicSDK to filter related logs on multiple hosts.
Requires: fabric, compatible with fabric 1.x & 2.x
"""

from fabric2 import SerialGroup

from base import print_result
from setting import LOG_PATH, HOSTS


def cd_and_run(c, cmd, path=None):
    if not cmd:
        return ""

    if path:
        cmd = "cd {} && {}".format(path, cmd)
    result = c.run(cmd, hide=True)
    return result.stdout or result.stderr


def main(cmd):
    for cxn in SerialGroup(*HOSTS):
        print_result(cxn.host, cd_and_run(cxn, cmd, path=LOG_PATH))


if __name__ == '__main__':
    _cmd = 'hostname'
    main(_cmd)

