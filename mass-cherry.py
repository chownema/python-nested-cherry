'''
Cherry pick up to certain
commit over a nested folder struct
'''

import sys
import os
import subprocess

def main(target, is_nested, from_commit_id, to_commit_id):
    msg = str(target) + str(is_nested) + str(from_commit_id) + str(to_commit_id)
    print str("args") + msg
    print str("Printing Files.... from target dir / files") + str(target)
    # print next(os.walk('../electron-quick-start'))[1]
    # print next(os.walk('../electron-quick-start'))[2]
    for root, dirs, files in os.walk("../electron-quick-start", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        # for name in dirs:
        #     print(str("Dir") + os.path.join(root, name))

# target = sys.argv[0] # is file or dir name
# is_nested = sys.argv[1] # toggle crawling nested folders
# from_commit_id = sys.argv[2] # Id string from 
# to_commit_id = sys.argv[3] # Id string to

target = input('Target ') # is file or dir name
is_nested = input('Is nested ') # toggle crawling nested folders
from_commit_id = input('From commit id ') # Id string from 
to_commit_id = input('To commit id ') # Id string to

main(target, is_nested, from_commit_id, to_commit_id)