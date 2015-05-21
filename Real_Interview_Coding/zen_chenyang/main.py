__author__ = 'daming'
class WordNode:
    def __init__(self, w):
        self.word = w
        self.chain_length = 1

    def __repr__(self):
        result = '(' + self.word + ',' + str(self.chain_length) + ')'
        return result

def longest_chain(w):
    my_hash = {}
    for i in range(0, len(w)):
        print w[i]
        obj = WordNode(w[i])
        if len(w[i]) in my_hash:
            my_hash[len(w[i])].append(obj)
        else:
            my_hash[len(w[i])] = list()
            my_hash[len(w[i])].append(obj)

    print my_hash

    

w = ['a','b','ba','bca','bda','bdca']
longest_chain(w)