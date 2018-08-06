#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: multi_host_run
Version: 0.1
Author: luoxu34
Summary: A small tool for publicSDK to filter related logs on multiple hosts.
Requires: fabric, compatible with fabric 1.x & 2.x
"""

from fabric.api import env, run, cd, execute
from fabric.contrib.files import exists


from setting import LOG_PATH, HOSTS

env.timeout = 2  # 2秒连接超时
env.hosts = HOSTS
env.dedupe_hosts = True  # 主机去重
env.skip_bad_hosts = True  # 跳过连不上的主机
env.abort_on_prompts = True  # 取消交互模式


def print_result(host, context):
    title = "{0} {1} {0}".format("=" * 34, host)
    print(title)
    print(context)
    print(title)
    print('\n\n')


def run_cmd(cmd, path=None):
    result = ""
    if not cmd:
        print_result(env["host"], result)
        return

    if LOG_PATH and exists(LOG_PATH):
        with cd(path):
            result = run(cmd)
    else:
        result = run(cmd)
    print_result(env["host"], result)
    return


if __name__ == "__main__":
    _cmd = "pwd"
    execute(run_cmd, _cmd, LOG_PATH)

