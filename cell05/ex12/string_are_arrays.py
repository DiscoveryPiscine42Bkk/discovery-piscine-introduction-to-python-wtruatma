#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(sys.argv) == 0:
        print("none")
else:
    combined = ''.join(args)
    z_chars = [char for char in combined if char == 'z']
    if len(z_chars) == 0:
        print("none")
    else:
         print('' .join(z_chars))
