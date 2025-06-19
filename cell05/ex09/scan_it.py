#!/usr/bin/env python3
import sys

argv = sys.argv[1:]

if len(argv) != 2:
    print("none")
else:
    word = argv[0]
    text = argv[1]
    count = text.split().count(word)
    print(count)
    