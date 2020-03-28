#!/bin/bash

function create()
{
    python3 ~/Projects/project_initializer/create.py $1
    cd ~/Projects/$1
    git init
    git remote add origin git@github.com:Ishan1742/$1.git #Make sure that you are having a ssh key login to GitHub. 
                                                          #If you want to use https then change the above line to
                                                          #git remote add origin https://github.com/Ishan1742/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}