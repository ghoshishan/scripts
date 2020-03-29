#!/bin/bash

set -e

programname=$0

display_usage() {
    echo "usage: $programname [-f path/]"
    echo "  -d path/    specify path to directory"
    echo "  -f path/    specify path to file"
    exit 1
}

if [ $# -le 1 ]; then
    display_usage
    exit 1
fi

if [[ ($# == "--help") || $# == "-h" ]]; then
    display_usage
    exit 0
fi

read -r -p "Are you sure? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    if [ "$1" == "-d" ]; then
        cd $2
        for file in *; do
            modi_date=$(date -r "$file" +"%Y-%m-%d")
            if [[ "$file" =~ "${modi_date}_".* ]]; then
                :
            else
                echo "${modi_date}_${file}"
                mv "${file}" "${modi_date}_${file}"
            fi
            #filename=$(echo "$file" | sed 's/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]_//')
            #echo "${filename}"
            #   rename 's/^\d{8}\-\d{2}\-\d{2}\_//' *
        done
    fi

    if [ "$1" == "-f" ]; then
        file="$2"
        modi_date=$(date -r "$file" +"%Y-%m-%d")
        if [[ "$file" =~ "${modi_date}_".* ]]; then
            :
        else
            echo "${modi_date}_${file}"
            mv "${file}" "${modi_date}_${file}"
        fi
    fi
else
    exit 1
fi
