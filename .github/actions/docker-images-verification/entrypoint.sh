#!/bin/sh -l

ls -lrt
python docker-images-verify --images-file ./docker_images.txt
