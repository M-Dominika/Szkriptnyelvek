#!/usr/bin/env python3

import sys

s=sys.argv[1]
i=s.find("\\n")
if i!=-1:
    s=s.replace(s[i:i+2],"")
if len(sys.argv)>2:
    s+=sys.argv[2]
print(s)
