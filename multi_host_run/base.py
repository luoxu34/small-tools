# -*- coding: utf-8 -*-

LOG_PATH = '/data/www/sdk_validator_server'

# publicSDK Hosts
HOSTS = [
    'duni@127.0.0.1:22',
]


def print_result(host, context):
    title = '{0} {1} {0}'.format('=' * 34, host)
    print(title)
    print(context)
    print(title)
    print('\n\n')
