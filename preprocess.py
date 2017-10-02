#!env python3

import re, sys

cname = None

def eprint(s):
    print(s, file=sys.stderr)

sourcepath = sys.argv[1]

buffer = ''
class_pat = re.compile('^(public )?class (?P<name>\w+)')

sfile = open(sourcepath, 'r')

for line in sfile:
    m = class_pat.match(line)
    if m is not None:
        cname = m.group('name')
        print(cname)
        break

sfile.close()

if cname is None:
    eprint("Could not extract class name from source.")
    exit(1)
