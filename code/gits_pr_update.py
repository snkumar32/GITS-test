import os
import sys
import subprocess
import argparse
from subprocess import Popen, PIPE


def gits_pr_update(args):
   #print(args)
    print("Hello from GITS command line tools- PR Update")

    flag = 0
    try:
        Untracked_file_check_status = list()
        Untracked_file_check_status.append("git")
        Untracked_file_check_status.append("status")

        Untracked_file_check = list()
        Untracked_file_check.append("grep")
        Untracked_file_check.append("Untracked files")

        process1 = subprocess.Popen(Untracked_file_check, stdout=PIPE, stderr=PIPE)
        process11 = subprocess.Popen(Untracked_file_check_status, stdin=process1.stdout,
                                         stdout=PIPE, stderr=PIPE)
        stdout, stderr = process11.communicate()
        #print(stdout)
        if (format(stdout) is not None):
            print("Note: Please commit uncommitted changes")
            #git stash
            exit()

        if flag == 0:
            print("Checking if upstream is set...")
            process2 = subprocess.Popen(['git', 'remote', '-vv'], stdout=PIPE, stderr=PIPE)
            process21 = subprocess.Popen(['grep', 'upstream'], stdin=process1.stdout,
                                     stdout=PIPE, stderr=PIPE)
            stdout, stderr = process21.communicate()

            if stdout is not None:
                 print("Upstream set")
            elif not stdout and args.upstream:
                print("Setting upstream")
                process3 = subprocess.Popen(['git', 'remote', 'add', 'upstream'], stdout=PIPE, stderr=PIPE)
                stdout, stderr = process3.communicate()
            else:
                print("Set --upstream")
                exit()

            process4 = subprocess.Popen(['git', 'checkout', 'master'], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process4.communicate()
            process5 = subprocess.Popen(['git', 'pull', 'upstream', 'master'], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process5.communicate()
            process6 = subprocess.Popen(['git', 'push', 'origin', 'master'], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process6.communicate()

        else:
            exit()

    except Exception as e:
        print("ERROR: gits sync command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
