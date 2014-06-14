#!/bin/sh
# 
# Convert beedoc files to markdown.

for file in bd/*.bd
do
	echo "Transforming $file..."
	mdfile="${file%.*}.md"
	beedoc -m $file > $mdfile
done

