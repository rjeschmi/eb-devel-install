#!/usr/bin/env python


import os
from multiprocessing import Pool
from subprocess import Popen, PIPE

branchexception = { 
    'vsc-base': 'master',
    'easybuild': 'master',
    'easybuild-wiki': 'master' }

def gitfetch(repo):
    process = Popen( ["git", "fetch", "--all" ], cwd=repo, stdout=PIPE, stderr=PIPE)
    output = process.communicate()[0]
    return "fetching %s output: %s" % (repo, output)

def gitmerge(repo):
    defbranch = branchexception.setdefault(repo, "develop")
    process = Popen( ["git", "merge", "--ff-only", "origin/"+defbranch ], cwd=repo, stdout=PIPE, stderr=PIPE)
    output = process.communicate()[0]
    return "fetching %s output: %s" % (repo, output)

def gitdefcheck(repo):
    defbranch = branchexception.setdefault(repo, "develop")
    process = Popen( ["git", "checkout", defbranch ], cwd=repo, stdout=PIPE, stderr=PIPE)
    output = process.communicate()[0]
    return "merging %s output: %s" % (repo, output)
   

def printoutput(out):
    for x in out:
        print x
 
if __name__ == '__main__':
    print "creating a 4 process pool"
    pool = Pool(processes=4)
    dirs = filter(os.path.isdir, os.listdir("."))
    print "applying gitfetch to %s" % dirs
    printoutput(pool.map(gitdefcheck, dirs))
    printoutput( pool.map(gitfetch, dirs))
    printoutput( pool.map(gitmerge, dirs))
            


