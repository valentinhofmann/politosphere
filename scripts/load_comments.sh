#!/bin/bash

FILEPATH=$1
YEAR=$2

for FILE in $FILEPATH/comments_$YEAR*
do	
	python -u load_comments.py --file $FILE &
done
wait
