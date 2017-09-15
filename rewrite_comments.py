#!/usr/bin/python

# Copyright 2017 The Fuchsia Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os

with open(sys.argv[1]) as f:
  lines = f.readlines()

# Remove the \n from the file
lines = [x.strip() for x in lines]

filename = sys.argv[1]

# Place this into a group
groupname = "Uncategorized"

# This is currently a curation. TODO : read the module name and
# only use the table below as an override.

if filename.find('media/fidl') != -1:
  groupname = 'Media'
elif filename.find('app/fidl') != -1:
  groupname = 'Lifecycle'
elif filename.find('fidl/compiler') != -1:
  groupname = 'Compiler'
elif filename.find('shadertoy') != -1:
  groupname = 'Shadertoy'
elif filename.find('scenic/fidl') != -1 or filename.find('images/fidl') != -1:
  groupname = 'Scenic'
elif filename.find('icu_data/fidl') != -1:
  groupname = 'ICU'
elif filename.find('auth/fidl') != -1:
  groupname = "Auth"
elif filename.find('fonts/fidl') != -1:
  groupname = "Fonts"
elif filename.find('netstack/fidl') != -1:
  groupname = "Netstack";
elif filename.find('input/fidl') != -1:
  groupname = "Input"
elif filename.find("views/fidl") != -1:
  groupname = "Views"
elif filename.find('network/fidl') != -1:
  groupname = "Network"
elif filename.find('netconnector/fidl') != -1:
  groupname = "NetConnector"
elif filename.find('power/fidl') != -1:
  groupname = "Power"
elif filename.find('presentation/fidl') != -1:
  groupname = "Presenter"

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
print '/*! @}} */'