#!/usr/bin/env python
"""
A simple module to update easybuild repository
"""

import os
import sys
from multiprocessing import Pool
from subprocess import Popen, PIPE

BRANCHEXCEPTION = {
    'vsc-base': 'master',
    'easybuild': 'master',
    'easybuild-wiki': 'master'
}

def gitfetch(repo):
    """fetch each repo by changing into the directory"""
    process = Popen(
        ["git", "fetch", "--all"], cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    return "fetching %s output: %s" % (repo, output)

def gitmerge(repo):
    defbranch = BRANCHEXCEPTION.setdefault(repo, "develop")
    process = Popen(
        ["git", "merge", "--ff-only", "origin/"+defbranch],
        cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    return "fetching %s output: %s" % (repo, output)

def gitdefcheck(repo):
    defbranch = BRANCHEXCEPTION.setdefault(repo, "develop")
    process = Popen(["git", "checkout", defbranch ], cwd=repo, stdout=PIPE, stderr=PIPE)
    output = process.communicate()[0]
    return "merging %s output: %s" % (repo, output)


def printoutput(out):
    for line in out:
        print line

def main():
    print "creating a 4 process pool"
    pool = Pool(processes=4)
    dirs = [repo for repo in os.listdir(".") if os.path.isdir(repo)]
    print "applying gitfetch to %s" % dirs
    printoutput(pool.map(gitdefcheck, dirs))
    printoutput(pool.map(gitfetch, dirs))
    printoutput(pool.map(gitmerge, dirs))

if __name__ == '__main__':
    main()
