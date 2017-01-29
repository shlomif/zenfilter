# * Write "zenfilter" (working title) for:
# - Displaying a "COUNT\t\d+" message every --count-step=\d+ lines.
# - Displaying the last --last=\d+ lines as "LAST\t.*"
# - Displaying lines matching --filter=.* (regex) as "FOUND\t.*"
# "make | python zenfilter.py [args]"

import sys
import argparse
import re

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count-step", type=int)
    parser.add_argument("--last", type=int)
    parser.add_argument("--filter")
    return parser.parse_args()

def zenfilter():
    args = getArgs();
    lastlines = []
    for index, line in enumerate(sys.stdin):
        if args.last:
            # Append a line to the last lines queue
            lastlines.append(line)
            if len(lastlines) > args.last:
                # Overflow reached. Remove the first line in the queue.
                lastlines.pop(0)

        if args.count_step and index % args.count_step == 0:
            # Line counter
            print("COUNT\t{}".format(index))
        
        if args.filter and re.search('(%s)' % args.filter, line):
            # Regex match. Print the line with the "FOUND" prefix.
            print("FOUND\t{}".format(line), end="")
    
    # Now we print the last lines queue
    for line in lastlines:
        print("LAST\t{}".format(line), end="")

if __name__ == "__main__":
    zenfilter()
