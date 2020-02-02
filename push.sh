#!/bin/bash

git add -A
git commit -m "test" --author="LeonardoBaroncelli <leonardo.baroncelli@inaf.it>"


tag="1.0.1"


git tag -d $tag

git push originlb --delete $tag

git tag $tag $(git log --format="%H" -n 1)
 
git push originlb $tag
