#!/bin/bash

git stash push -u -m "Stashing before sync"
git fetch origin main
git reset --hard origin/main
git stash pop --index
git stash drop
