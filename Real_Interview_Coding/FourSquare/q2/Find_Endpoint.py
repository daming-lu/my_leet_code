__author__ = 'daming'
import fileinput
import sys

class Solution:
    def getPathTokens(self, path):
        tokens = []
        last_index = 0
        i = 1
        while i < len(path):
            i = path.find('/', last_index+1)
            if i==-1:
                break
            tokens.append(path[last_index:i])
            last_index = i
            i += 1
        tokens.append(path[last_index:])
        return tokens

    

    def buildHash(self, file_name):
        try:
            file_handle = open(file_name, "r")
        except IOError:
            print >> sys.stderr, "Cannot open config file", file_name
            sys.exit(1)

        self.pathTokenHash = {}
        for line in iter(file_handle):
            line = line.strip()
            pieces = line.split(' ')
            print pieces
            dir_tokens = self.getPathTokens(pieces[0])
            print 'dir_tokens : ', dir_tokens
            curTokenNode = self.pathTokenHash
            for token in dir_tokens:
                if token not in curTokenNode:
                    curTokenNode[token] = {}
                curTokenNode = curTokenNode[token]
            curTokenNode = pieces[1]



    def findEndpoint(self):
        return []

obj = Solution()
print obj.buildHash(sys.argv[1])