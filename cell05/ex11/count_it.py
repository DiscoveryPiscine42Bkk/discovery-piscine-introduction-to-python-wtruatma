#!/usr/bin/env python3
import sys

def main():
    params = sys.argv[1:]
    if len(params)== 0:
        print ("none")
    else:
        print(f"parameters:{len(params)}")
        for p in params:
            print(f"{p}:{len(p)}")
main()
             
