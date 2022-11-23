import subprocess
import sys

img_path = sys.argv[1]
# node_path = "C:\\Program Files\\nodejs"

with open("Creds.txt", "r") as f:
    apiKey = f.readline()
    apiSec = f.readline()
    jwt = f.readline()

def pin_img_to_pinata(img_path):
    ipfs_hash = subprocess.check_output(['node','./_pinImgToPinata.js', img_path])
    return ipfs_hash.decode().strip()



print(pin_img_to_pinata(img_path))