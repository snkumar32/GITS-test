import os
import sys
import subprocess
import argparse

def gits_pr_update(args):
    print(args)
    print("Hello from GITS command line tools- PR Update")
    upstream_check = os.popen("git remote -vv | grep upstream").read()
    print(upstream_check)
    if upstream_check:
        print("Upstream set")
    elif not upstream_check and args.upstream:
        print("Setting upstream")
        rc = os.popen("git remote add upstream " + args.upstream)
        print(os.popen("git remote -vv | grep upstream").read())
    else:
        print("Set --upstream")
        exit()

    checkout = os.popen("git checkout master").read()
    upstream_pull = os.popen("git pull upstream master").read()
    origin_push = os.popen("git push origin master").read()




    




