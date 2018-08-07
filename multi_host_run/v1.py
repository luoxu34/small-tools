#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import env, run, cd, execute
from fabric.contrib.files import exists
from fabric.state import output

from base import PasswordException, print_result, HOSTS, LOG_PATH


env.timeout = 2  # 2秒连接超时
env.hosts = HOSTS
env.dedupe_hosts = True      # 主机去重
env.skip_bad_hosts = True    # 跳过连不上的主机
env.abort_on_prompts = True  # 取消交互模式
env.abort_exception = PasswordException
output.aborts = False        # 取消Fatal error输出


def cmd_help(cmd, path=''):
    result = ''
    if not cmd:
        print_result(env['host'], result)
        return

    try:
        if path and exists(path):
            with cd(path):
                result = run(cmd, quiet=True)
        else:
            result = run(cmd, quiet=True)
    except PasswordException as exc:
        result = exc.message

    print_result(env['host'], result)


def main(cmd, path=LOG_PATH):
    execute(cmd_help, cmd, path)


if __name__ == '__main__':
    main('pwd')

