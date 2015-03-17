__author__ = 'daming'
import fileinput
import sys

class Solution:
    def buildHash(self, file_name):
        try:
            file_handle = open(file_name, "r")
        except IOError:
            print >> sys.stderr, "Cannot open config file", file_name
            sys.exit(1)

        self.endpointHash = {}
        for line in iter(file_handle):
            line = line.strip()
            pieces = line.split(' ')
            print pieces

    def findEndpoint(self):
        return []

obj = Solution()
print obj.buildHash(sys.argv[1])