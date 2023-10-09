#!/bin/bash

SCRIPT_DIR=$(pwd)
REPO_DIR="$SCRIPT_DIR/repo"

mkdir -p $REPO_DIR
cd $REPO_DIR
git --git-dir="$REPO_DIR/.git" --work-tree="$REPO_DIR" checkout HEAD

COMMIT_DIR="$SCRIPT_DIR/morse-files"
mkdir -p $COMMIT_DIR

COMMITS=($(git --git-dir="$REPO_DIR/.git" log --reverse --format=%H))

for ((i=0; i<${#COMMITS[@]}; i++))
do
    COMMIT="${COMMITS[$i]}"
    COMMIT_HASH="${COMMIT:0:7}"
    
    echo "checking out commit $i with hash $COMMIT_HASH to $COMMIT_DIR"
    cd $REPO_DIR
    git --git-dir="$REPO_DIR/.git" --work-tree="$REPO_DIR" checkout $COMMIT

    IDX=$(echo $i | awk '{printf "%04d", $1}')
    
    echo "  data SHA256 -> $(cat data | sha256sum)"
    mkdir -p "$COMMIT_DIR/$IDX-$COMMIT_HASH"
    cp data $COMMIT_DIR/$IDX-$COMMIT_HASH
    # cp data "$COMMIT_DIR/data-$IDX-$COMMIT_HASH.wav"

    # if [ $i -eq 2 ]; then
    #     echo 'smoke test done.'
    #     break
    # fi
done

# reset back to latest commit
cd $REPO_DIR
git checkout e2483776f7011364f613a64e05201b66b1aa2997

cd $SCRIPT_DIR
echo Done.
