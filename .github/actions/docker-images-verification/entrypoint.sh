#!/bin/sh -l

ls -lrt
./docker-images-verify --images-file ./docker_images.txt
