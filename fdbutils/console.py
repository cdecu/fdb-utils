#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of fdbutils.
# https://github.com/cdecu/fdb-utils

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 1992-2016, Carlos de Cumont <carlos@decumont.be>

import os, argparse, logging
# import re
# import fdb
#from fdbutils import Table, dialect_names

fdb_descr = """
Firebird utility command
"""

parser = argparse.ArgumentParser(
    prog="fdbutils",
    description=fdb_descr,
    epilog="\nbe carefull and good lock !\n",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80))


parser.add_argument('--server', help='Server Address', type=str, default='localhost')
parser.add_argument('--port', help='Server Port', type=int, default=3050)
parser.add_argument('--user', help='User Name', type=str, default=os.getenv("isc_user", "SYSDBA"))
parser.add_argument('--pwd', help='User Password', type=str, default=os.getenv("isc_password", "1"))
parser.add_argument('--db', help='Database', type=str, default=os.getenv("isc_database", "/srv/firebird/employee.fdb"))
parser.add_argument('--show', nargs="*", metavar="x", help="tables views procedures OneTable ...")
parser.add_argument('--drop', nargs="*", metavar="x", help="tables views procedures OneTable ...")
parser.add_argument('-l', '--log', type=str.upper, help='log level (CRITICAL, FATAL, ERROR, DEBUG, INFO, WARN)', default='WARN')


def set_logging(args):
    try:
        loglevel = int(getattr(logging, args.log))
    except (AttributeError, TypeError):
        raise NotImplementedError('log level "%s" not one of CRITICAL, FATAL, ERROR, DEBUG, INFO, WARN' % args.log)
    logging.getLogger().setLevel(loglevel)


def ArgumentParser(args) -> str:
    set_logging(args)
    logging.info(str(args))
    if args.show:
        print("show", args.show)
        return "show"
    return ""


def show(items:list) -> object:
    # class CustomDict(dict):
    #     def __getattr__(self, name):
    #         return self[name]
    #
    # p = CustomDict(user='James', location='Earth')
    # print
    # p.user
    # print
    # p.location
    print(type(items))
    print(items)
    pass


def drop(items: list) -> object:
    # class CustomDict(dict):
    #     def __getattr__(self, name):
    #         return self[name]
    #
    # p = CustomDict(user='James', location='Earth')
    # print
    # p.user
    # print
    # p.location
    print(type(items))
    print(items)
    pass


def generate(args=None):
    if not args:
        args = parser.parse_args()
    action = ArgumentParser(args)
    if action == "show":
        exit(show(args.show))
    elif action == "drop":
        exit(drop(args.show))
    else:
        parser.print_help()
        exit(-1)

if __name__ == '__main__':
    generate()
