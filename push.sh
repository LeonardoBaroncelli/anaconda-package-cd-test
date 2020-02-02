#!/bin/bash

git add -A
git commit -m "test" --author="LeonardoBaroncelli <leonardo.baroncelli@inaf.it>"


#tag=$(git describe --tags)


git tag -d v1.0.0

git push originlb --delete v1.0.0

git tag v1.0.0 $(git log --format="%H" -n 1)
 
git push originlb v1.0.0
