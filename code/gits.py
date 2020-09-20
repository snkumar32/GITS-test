import os
import sys
import argparse
from gits_pr_update import gits_pr_update

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_pr_subparser= subparsers.add_parser('sync3335', help='sync help')
gits_pr_subparser.set_defaults(func=gits_pr_update)
gits_pr_subparser.add_argument('--upstream', nargs='?')
args = parser.parse_args()
args.func(args)

