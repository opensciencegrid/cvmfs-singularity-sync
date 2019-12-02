#!/bin/sh -l

#echo "Hello $1"
#time=$(date)
echo "Hello"
#echo ::set-output name=time::$time
python docker-images-verify --images-file ./docker_images.txt
