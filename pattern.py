#!/usr/bin/env python2
import sys
import string


def create(length):
    if length>20280:
        return "Maximum limit exceeded"
    pattern=""
    for i in range(10):
        for j in list(string.lowercase):
            for k in list(string.uppercase):
                pattern=pattern+str(i)+str(j)+str(k)
                if len(pattern)>=length:
                    return pattern[:length]

def offset(pattern):
    if pattern[0:2]=='0x':
        pattern=pattern[2:].decode('hex')[::-1]
    if len(pattern)<3:
        return "We need a pattern of length at least 3 to accurately determine the offset"

    offset=create(20280).find(pattern)
    if offset==-1:return "Pattern not found"
    else: return "Perfect match at offset "+str(offset+1)

if len(sys.argv)==1:
    print '''Usage:
     ./{} [options]

     -l <length> Specify the length             The length of the pattern, limit 20280
     -q, --query Aa0A                           Query to Locate
     '''.format(sys.argv[0])
else:
    if sys.argv[1]=='-l':
        print create(int(sys.argv[2]))
    if sys.argv[1]=='-q':
        print offset(str(sys.argv[2]))