#!/bin/bash

FILES="./*"

LoopFiles () {

	arg1=*

	for f in $arg1
	do
		if [ -f $f ]
		then

			echo "****git update-index --assume-unchanged $f"
			git update-index --assume-unchanged $f
			
		elif [ -d $f ]
		then
			echo "directory $f"
			git update-index --assume-unchanged $f"/"
			cd $f
			LoopFiles 
		fi
	done
	
	cd ..

}


LoopFiles $FILES


