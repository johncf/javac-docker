#!env python3

# original: https://stackoverflow.com/a/8022469/2849934

import re, subprocess, sys
from os.path import dirname, abspath

cname = None
jfile = None

def eprint(s):
    print(s, file=sys.stderr)

buffer = ''
class_pat = re.compile('^(public )?class (?P<name>\w+)')

for line in sys.stdin:
    if jfile is None:
        buffer += line
        m = class_pat.match(line)
        if m is not None:
            cname = m.group('name')
            eprint("class name: " + cname)
            fpath = dirname(abspath(__file__)) + '/workdir/' + cname + '.java'
            eprint("java file: " + fpath)
            jfile = open(fpath, 'w')
            jfile.write(buffer)
    else:
        jfile.write(line)

if jfile is None:
    eprint("Could not extract class name from source.")
    exit(1)

jfile.close()

cfile = open('workdir/classname', 'w')
cfile.write(cname)
cfile.close()
