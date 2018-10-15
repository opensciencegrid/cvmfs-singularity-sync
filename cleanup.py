"""
Cleanup for Singularity container

Scan the images in the singularity CVMFS.  If an image directory has not been "linked" to for 2 days, 
remove the image directory.

Maintains state in a file in the root singularity directory named .missing_links.json

"""
import glob
import os
import json
import datetime
import dateutil.parser
import shutil
import argparse

json_location = "/cvmfs/singularity.opensciencegrid.org/.missing_links.json"
#json_location = "missing_links.json"

# JSON structure:
# {
#   "missing_links": {
#       "/cvmfs/singularity.opensciencegrid.org/.images/7d/ba009871baa50e01d655a80f79728800401bbd0f5e7e18b5055839e713c09f": "<timestamp_last_linked>"
#       ...
#   }
# }

def cleanup(delay=2, test=False):
    '''Clean up unlinked singularity images'''
    # Read in the old json, if it exists
    json_missing_links = {}
    if os.path.exists(json_location):
        with open(json_location) as json_file:
            json_missing_links = json.loads(json_file.read())['missing_links']

    # Get all the images in the repo

    # Walk the directory /cvmfs/singularity.opensciencegrid.org/.images/*
    image_dirs = glob.glob("/cvmfs/singularity.opensciencegrid.org/.images/*/*")

    # Walk the named image dirs
    named_image_dir = glob.glob("/cvmfs/singularity.opensciencegrid.org/*/*")

    # For named image dir, look at the what the symlink points at 
    for named_image in named_image_dir:
        link_target = os.readlink(named_image)
        # Multiple images can point to the same image_dir
        if link_target not in image_dirs:
            print("%s not in list of image directories from %s" % (link_target, named_image))
        else:
            image_dirs.remove(link_target)

    # Now, for each image, see if it's in the json
    for image_dir in image_dirs:
        if image_dir in json_missing_links:
            image_dirs.remove(image_dir)
        else:
            # Add it to the json
            print("Newly found missing link: %s" % (image_dir))
            json_missing_links[image_dir] = str(datetime.datetime.now())

    # Loop through the json missing links, removing directories if over the `delay` days
    for image_dir, last_linked in json_missing_links.items():
        date_last_linked = dateutil.parser.parse(last_linked)
        if date_last_linked < (datetime.datetime.now() - datetime.timedelta(days=delay)):
            # Remove the directory
            print("Removing missing link: %s" % image_dir)
            if not test:
                shutil.rmtree(image_dir)
                del json_missing_links[image_dir]

    # Write out the end json
    with open(json_location, 'w') as json_file:
        json_file.write(json.dumps({"missing_links": json_missing_links}, default=str))



def main():
    '''Main function'''
    args = parse_args()
    cleanup(test=args.test)

def parse_args():
    '''Parse CLI options'''
    parser = argparse.ArgumentParser()

    parser.add_argument('--test', action='store_true',
                        help="Don't remove files, but go through the motions of removing them.")
    return parser.parse_args()

if __name__ == "__main__":
    main()
