#!/usr/bin/python

# Copyright 2017 The Fuchsia Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

# convert the // comments in the .fidl files into
# doxygen-style comments. This script is meant to be
# called by the doxygen process as an input filter for 
# each file to process.

with open(sys.argv[1]) as f:
  lines = f.readlines()

# Remove the \n from the file
lines = [x.strip() for x in lines] 

# we're going to look for the first tokens on the line to be 
# '//' to start.
in_comment = False
for line in lines:
  index = line.find('//')
  if index >= 0:
    # found '//'
    if in_comment == True:
      print '* {0}'.format(line[index+2:])
    else:
      print '/**'
      print '* {0}'.format(line[index+2:])
      in_comment = True
  else:
    # no '//''
    if in_comment == True:
      in_comment = False;
      print '*/'
    print line






