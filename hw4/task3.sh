#!/bin/bash

# Ensures the input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Check if the file exists
if [ ! -f "$1" ]; then
    echo "File not found!"
    exit 1
fi

# Processing the data, skipping the header with NR>1
awk -F, 'NR > 1 && $3 == "2"' $1 |
awk '{gsub(/[[:space:]]+$/, ""); if ($0 ~ /S$/) print}' |
awk -F, '{ gsub("female", "F"); gsub("male", "M"); print $0 }' |
awk '{ print }' | tee >(
awk -F, 'BEGIN { sum=0; count=0 } 
         { if ($7 != "" && $7+0 == $7) { sum+=$7; count++ } }
	 END { if (count > 0) { print "Average Age: " sum / count } else { print "No valid data for average age calculation." } }')
