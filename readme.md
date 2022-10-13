# ALAC-converter

This is just a tiny Python script used to convert a record collection from various formats to ALAC. 
It takes a list of files as input (`find ! -type d`), and loops over this list. 

The directory structure is mirrored in the new destination, any non-audio files is copied over. 
Audio files (matching a list of extensions) are converted if they doesn't already exist. 

At the end, the script will print a list of formats and the number of files copied. 

It can probably be done better and easier and as a single line in Bash, but it's always nice to play with Python just to see what little I remember. 


Feel free to use or improve! 


