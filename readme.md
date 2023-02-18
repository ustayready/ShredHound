ShredHound
==================

## Overview ##
Split a large BloodHound JSON file into a bunch of smaller files for faster importing.

Follow me on Twitter ([Mike Felch - @ustayready](https://twitter.com/ustayready)) 

## Basic Usage ##
### Requires OpenAI API key
```
usage: shred.py [-h] --output OUTPUT --filename FILENAME [--chunks CHUNKS]

optional arguments:
  -h, --help           show this help message and exit
  --output OUTPUT      Output folder for chunked JSON files
  --filename FILENAME  Name of the BloodHound JSON file
  --chunks CHUNKS      Number of chunks to split the BloodHound JSON file
                       into
  
ShredHound the BloodHound JSON splitter
```
*python shred.py --filename /tmp/output.json --chunks 100 --output /tmp/*
         
## Installation ##
You can install and run with the following command:

```bash
$ git clone https://github.com/ustayready/shredhound
$ cd shredhound
~/shredhound $ virtualenv -p python3 .
~/shredhound $ source bin/activate
(shredhound) ~/shredhound $ python shred.py
```




