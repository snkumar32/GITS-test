import os
import sys
import subprocess
import argparse
from subprocess import Popen, PIPE


def gits_pr_update(args):
   #print(args)
    #print("Hello from GITS command line tools- PR Update")
    #flag = 0
    try:
        Untracked_file_check_status = list()
        Untracked_file_check_status.append("git")
        Untracked_file_check_status.append("status")
        Untracked_file_check_status.append("--porcelain")

        #Untracked_file_check = list()
        #Untracked_file_check.append("grep")
        #Untracked_file_check.append("Untracked files")

        process1 = subprocess.Popen(Untracked_file_check_status, stdout=PIPE, stderr=PIPE)
        #process11 = subprocess.Popen(Untracked_file_check, stdin=process1.stdout, stdout=PIPE, stderr=PIPE)

        stdout, stderr = process1.communicate()
        #print(format(stdout))
        if stdout != b'':
            print("Note: Please commit uncommitted changes")
            #git stash
            exit()

        print("Checking if upstream is set..")
        process2 = subprocess.Popen(['git', 'remote', '-vv'], stdout=PIPE, stderr=PIPE)
        process21 = subprocess.Popen(['grep', 'upstream'], stdin=process2.stdout, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process21.communicate()

        if stdout != b'':
            print("Upstream set")
        elif stdout == b'' and args.upstream:
            print("Setting upstream")
            process3 = subprocess.Popen(['git', 'remote', 'add', 'upstream', args.upstream], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process3.communicate()
        else:
            print("Set --upstream")
            exit()

        print("Checkout master..")
        process4 = subprocess.Popen(['git', 'checkout', 'master'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process4.communicate()
        print(stdout.decode('utf-8'))
        print("Pull Changes from Upstream Master..")
        process5 = subprocess.Popen(['git', 'pull', 'upstream', 'master'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process5.communicate()
        print(stdout.decode('utf-8'))
        print("Push changes to local master..")
        process6 = subprocess.Popen(['git', 'push', 'origin', 'master'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process6.communicate()
        print(stdout.decode('utf-8'))


    except Exception as e:
        print("ERROR: gits sync command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
