import subprocess
from subprocess import PIPE


def gits_pr_update_func(args):
    # print(args)
    # print("Hello from GITS command line tools- PR Update")
    # flag = 0
    try:
        Untracked_file_check_status = list()
        Untracked_file_check_status.append("git")
        Untracked_file_check_status.append("status")
        Untracked_file_check_status.append("--porcelain")

        process1 = subprocess.Popen(Untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)

        stdout, stderr = process1.communicate()
        # print(format(stdout))
        if stdout != b'':
            print("Note: Please commit uncommitted changes")
            # git stash
            exit()

        print("Checking if upstream is set..")
        process2 = subprocess.Popen(['git', 'remote', '-vv'],
                                    stdout=PIPE, stderr=PIPE)
        process21 = subprocess.Popen(['grep', 'upstream'],
                                     stdin=process2.stdout,
                                     stdout=PIPE, stderr=PIPE)
        stdout, stderr = process21.communicate()

        if stdout != b'':
            print("Upstream set")
        elif stdout == b'' and args.upstream:
            print("Setting upstream")
            process3 = subprocess.Popen(['git', 'remote', 'add', 'upstream',
                                         args.upstream],
                                        stdout=PIPE,
                                        stderr=PIPE)
            stdout, stderr = process3.communicate()
        else:
            print("Set --upstream")
            exit()

        print("\nCheckout master..")
        checkout_master = list()
        checkout_master.append("git")
        checkout_master.append("checkout")
        checkout_master.append("master")
        process4 = subprocess.Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process4.communicate()
        print(stdout.decode('utf-8'))

        print("Pull Changes from Upstream Master..")
        pull_upstream = list()
        pull_upstream.append("git")
        pull_upstream.append("pull")
        pull_upstream.append("upstream")
        pull_upstream.append("master")
        process5 = subprocess.Popen(pull_upstream, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process5.communicate()
        print(stdout.decode('utf-8'))

        print("Push changes to local master..")
        push_origin = list()
        push_origin.append("git")
        push_origin.append("push")
        push_origin.append("origin")
        push_origin.append("master")
        process6 = subprocess.Popen(push_origin, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process6.communicate()
        print(stdout.decode('utf-8'), stderr.decode('utf-8'))

    except Exception as e:
        print("ERROR: gits sync command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
