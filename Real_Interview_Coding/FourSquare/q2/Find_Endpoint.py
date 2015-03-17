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
            dir_tokens = self.getPathTokens(pieces[0])
            curTokenNode = self.pathTokenHash
            for i in range(0, len(dir_tokens)):
                token = dir_tokens[i]
                if token not in curTokenNode:
                    curTokenNode[token] = {}
                curTokenNode = curTokenNode[token]
            curTokenNode[""] = pieces[1]

        self.findEndpoint()
        return ""

    def matchToken(self,tokens, curInd, curTokenNode):
        if curInd == len(tokens):
            return curTokenNode[""]
        if tokens[curInd] in curTokenNode:
            result = self.matchToken(tokens, curInd+1, curTokenNode[tokens[curInd]])
            if result != False:
                return result
            if '/X' in curTokenNode:
                return self.matchToken(tokens, curInd+1, curTokenNode['/X'])
            else:
                return False

        elif '/X' in curTokenNode:
            return self.matchToken(tokens, curInd+1, curTokenNode['/X'])
        else:
            return False

    def findEndpoint(self):
        for line in fileinput.input('-'):
            if line is None:
                continue
            dir_tokens = self.getPathTokens(line.strip())
            curTokenNode = self.pathTokenHash
            result = self.matchToken(dir_tokens,0,curTokenNode)
            if result == False:
                print '404'
            else:
                print result
        return []

obj = Solution()
print obj.buildHash(sys.argv[1])