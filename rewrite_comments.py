#!/usr/bin/python

# Copyright 2017 The Fuchsia Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
import re

filename = sys.argv[1]

with open(filename) as f:
  lines = f.readlines()

# Remove the \n from the lines
lines = [x.strip() for x in lines]

groupname = "Uncategorized"


# Try to find the group name, it will be of the form"
# module <name>;
# We replace the . with something that won't confuse doxygen.
for line in lines:
  if line.find('module') == 0:
    try:
      groupname = re.search('module[ *](.+?)[\;]' ,line).group(1).replace('.', '_')
    except AttributeError:
      groupname = 'Uncategorized'
      #print 'error!'
    #print groupname
    #sys.exit(0)
    break

# group header  
print '/*! \\addtogroup {0}\n * @{{\n */'.format(groupname)

# convert the // comments in the .fidl files into
# doxygen-style comments. This script is meant to be
# called by the doxygen process as an input filter for 
# each file to process.

in_comment = False
for line in lines:
  index = line.find('//')
  if index >= 0:
    # found '//'
    if in_comment == True:
      print ' * {0}'.format(line[index+2:])
    else:
      print '/*!'
      print ' * {0}'.format(line[index+2:])
      in_comment = True
  else:
    # no '//''
    if in_comment == True:
      in_comment = False;
      print ' */'
    print line

# group footer
print '/*! @} */'