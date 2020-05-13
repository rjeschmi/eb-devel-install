#!/usr/bin/env python
"""
A simple module to update easybuild repository
"""
    
import os
import sys
from multiprocessing import Pool
from subprocess import Popen, PIPE

update_dirs = {
    'eb/easybuild': {
        'branch': 'develop',
        'upstream'   : 'https://github.com/easybuilders/easybuild.git',
     },

    'eb/easybuild-easyblocks': { 
        'branch': 'develop',
        'upstream'   : 'https://github.com/easybuilders/easybuild-easyblocks.git',
        'origin'     : 'https://github.com/rjeschmi/easybuild-easyblocks.git',
     },
    'eb/easybuild-easyconfigs': {
        'branch': 'develop',
        'upstream'   : 'https://github.com/easybuilders/easybuild-easyconfigs.git',
        'origin'     : 'https://github.com/rjeschmi/easybuild-easyconfigs.git',
     },
    'eb/easybuild-framework': {
        'branch': 'develop',
        'upstream'   : 'https://github.com/easybuilders/easybuild-framework.git',
        'origin'     : 'https://github.com/rjeschmi/easybuild-framework.git',
    }
}

def gitaddupstream(repo):
    """update remote to each repo by changing into the directory"""
    process = Popen(
        ["git", "remote", "remove", "upstream"], cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    process = Popen(
        ["git", "remote", "remove", "origin"], cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    process = Popen(
        ["git", "remote", "add", "upstream", update_dirs[repo]['upstream']], cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    process = Popen(
        ["git", "remote", "add", "origin", update_dirs[repo]['origin']], cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    return "fetching %s output: %s" % (repo, output)


def gitfetch(repo):
    """fetch each repo by changing into the directory"""
    process = Popen(
        ["git", "fetch", "--all"], cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    return "fetching %s output: %s" % (repo, output)

def gitmerge(repo):
    process = Popen(
        ["git", "merge", "--ff-only", "upstream/"+update_dirs[repo]['branch']],
        cwd=repo, stdout=PIPE, stderr=PIPE
    )
    output = process.communicate()[0]
    return "fetching %s output: %s" % (repo, output)

def gitdefcheck(repo):
    process = Popen(["git", "checkout", update_dirs[repo]['branch'] ], cwd=repo, stdout=PIPE, stderr=PIPE)
    output = process.communicate()[0]
    return "merging %s output: %s" % (repo, output)


def printoutput(out):
    for line in out:
        print(line)

def main():
    print("creating a 4 process pool")
    pool = Pool(processes=10)
    dirs = update_dirs.keys()
    print("applying gitfetch to %s" % dirs)
    printoutput(pool.map(gitaddupstream, dirs))
    printoutput(pool.map(gitdefcheck, dirs))
    printoutput(pool.map(gitfetch, dirs))
    printoutput(pool.map(gitmerge, dirs))

if __name__ == '__main__':
    main()
