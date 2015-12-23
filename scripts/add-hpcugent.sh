#!/bin/bash


eb_repos=( "easybuild-framework" "easybuild-easyconfigs" "easybuild-easyblocks" "vsc-base")
eb_subdir="eb"

for repo in "${eb_repos[@]}"
do
   git_cmd="cd ${eb_subdir}/${eb_repo} && git remote add upstream git@github.com:hpcugent/${repo}.git"
   $(${git_cmd})
done
