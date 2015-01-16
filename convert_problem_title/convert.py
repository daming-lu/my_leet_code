__author__ = 'daming'
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

result = ""

sys.argv.pop(0)

while len(sys.argv) > 0 :
    result += sys.argv.pop(0).lower()
    if len(sys.argv) > 0:
        result += "_"

print "\n", result, "\n"

