#!/usr/bin/python3

import os
import sys
import cgi, cgitb

import cgitb; cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
arg1 = form['name'].value
arg1 = arg1.replace('..', '')
arg1 = arg1.replace('//', '')
filter = lambda x: x if x[0] != '/' else x[1:]
arg1 = filter(arg1)

src = './tmp/' + arg1
length = os.stat(str(src)).st_size

sys.stdout.write("Content-Type: image/png\n")
sys.stdout.write("Content-Length: " + str(length) + "\n")
sys.stdout.write("\n")
sys.stdout.flush()
sys.stdout.buffer.write(open(src, "rb").read())

