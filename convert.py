#!/usr/bin/python3
from hashlib import new
import os
import os.path
import subprocess
from wsgiref import validate
import shutil

# Feel free to use, copy or improve. Licensed under the MIT License.


files = open("files.txt", "r").readlines()
prefix = "/new/directory/path/prefix/"
oldPrefix = "/old/directory/prefix/"

validExts = ['.mp3', '.ogg', '.flac', '.wav', '.MP3', '.wma', '.shn']

formats = {}

count=0

for line in files:
    file = line.replace("\n", "")
    oldext = os.path.splitext(file)[1]


    if oldext in formats:
        formats[oldext]+=1
    else :
        formats[oldext] = 1

    # Get existing directory
    basedir = os.path.dirname(file)

    # Full path to existing file
    existingFile = (oldPrefix + file).replace("/./", "/")

    # Get new directory
    newpath = (prefix + basedir).replace("/./", "/")
    
    # Get new filename if we're converting
    newfile = (prefix + os.path.splitext(file)[0]).replace("/./", "/")
    newfile += ".m4a"

    # Old filename if we're copying
    oldFileNewLoc = (prefix + file).replace("/./", "/")

    if not os.path.exists(newpath):
        os.makedirs(newpath)


    # If valid audio file convert, if not copy files 
    if oldext in validExts:
        if not os.path.exists(newfile):
            print("Convert: " + existingFile + " to " + newfile)
            subprocess.run(["ffmpeg", "-i", existingFile, "-acodec", "alac", newfile])
        else:
            print("Skipping " + newfile)
    else:
        if not os.path.exists(oldFileNewLoc):
            print("Copy " + existingFile + " to " + oldFileNewLoc)
            shutil.copyfile(existingFile, oldFileNewLoc)
        else:
            print("Skipping " + oldFileNewLoc)

print(formats)
