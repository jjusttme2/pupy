# -*- coding: utf-8 -*-
# Copyright (c) 2015, Nicolas VERDIER (contact@n1nj4.eu)
# Pupy is under the BSD 3-Clause license. see the LICENSE file at the root of the project for the detailed licence terms
import shlex

__all__ = ['parse_transports_args']

def parse_transports_args(args, exit=True):
    args_dic = {}

    for val in shlex.split(args):

        tab = val.split('=', 1)
        if len(tab) != 2:
            message = 'Error: transport arguments must be in format NAME=VALUE or "NAME=value with spaces"'
            if exit:
                raise SystemExit(message)
            else:
                raise ValueError(message)

        args_dic[tab[0].lower()]=tab[1]

    return args_dic
