# Docker image text file verification docker action

This action verifies wheather the images in docker_iamges.txt file is valid, by requesting their manifests.

## Inputs

### `docker-images-file`

**Required** The name of the docker images file. Default docker_images.txt

## Outputs

### `time`

The time we greeted you.

## Example usage

```yaml
uses: ./actions/docker-images-verification@master
with:
  docker-iamges-file: './docker_images.txt'
```
