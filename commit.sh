#!/bin/bash

FILES="./*"

arg2=*

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

CDinto() { 
    cd ./thingy
    LoopFiles $FILES
}

CDinto $FILES

Commit () {

    #git rm -r --cached .
    git add *
    git commit -m "hasjd"
    git push
}


echo "Would you like to commit? (Yes/No)"
echo "you are in"

select yn in "Yes" "No"
do

    case $yn in 
        Yes ) Commit $arg2; break;;
        No ) exit;;
    esac
done