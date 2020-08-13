#!/bin/zsh

# @package
# @brief
# @author stfate

if [ $# -ne 1 ]; then 
    echo "usage: gen_new_post.sh <postname>" 1>&2
    exit 1
fi

cd content/posts
cp -r __template $1
