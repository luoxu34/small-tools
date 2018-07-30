#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import shutil


if __name__ == '__main__':

    argv = sys.argv[1:]
    if len(argv) != 1:
        print('usage: python %s your_json_file' % (__file__))
        exit(-1)

    _file = argv[0]
    if not os.path.isfile(_file):
        print('not file!')
        exit(-1)

    # backup file
    dstfile = os.path.join(_file + '.old')
    shutil.copyfile(_file, dstfile)

    with open(_file) as f:
        d = json.load(f)

    with open(_file, 'w') as f:
        json.dump(d, f, indent=1)
        print('ok...')

    exit(0)

