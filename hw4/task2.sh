#!/bin/bash

grep -l "sample" dataset1/* | while read file; do
    count=$(grep -o "CSC510" "$file" | wc -l)
    if [ "$count" -ge 3 ]; then
        filesize=$(stat -f%z "$file")
        echo "$file $count $filesize"
    fi
done | sort -k2,2nr -k3,3nr | gawk '{gsub("file_", "filtered_", $1); print $1, $2, $3}'


