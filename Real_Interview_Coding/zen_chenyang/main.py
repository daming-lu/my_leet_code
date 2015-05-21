__author__ = 'daming'
class WordNode:
    def __init__(self, w):
        self.word = w
        self.chain_length = 1

    def __repr__(self):
        result = '<' + self.word + ',' + str(self.chain_length) + '>'
        return result


def getSmallerWords(word):
    ans = []
    for i in range(0, len(word)):
        ans.append(word[0:i]+word[i+1:])
    return ans

def find_longest(my_hash):
    ans = 0
    keys = my_hash.keys()
    print keys
    for l in keys:
        if l-1 not in my_hash:
            continue
        cur_len_word_nodes = my_hash[l]
        for word_node in cur_len_word_nodes:
            words_1_char_less = getSmallerWords(word_node.word)
            cur_chain_length = word_node.chain_length
            for word_1_char_less in words_1_char_less:
                for word_node_1_less in my_hash[l-1]:
                    if word_node_1_less.word == word_1_char_less:
                        cur_chain_length = max(cur_chain_length, word_node_1_less.chain_length+1)
            word_node.chain_length = cur_chain_length
            if word_node.chain_length > ans:
                ans = word_node.chain_length
    return ans

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

    # print my_hash

    # return find_longest(my_hash)
    ans = find_longest(my_hash)

    # print 'after : ', my_hash
    return  ans

w_orig = ['a','b','ba','bca','bda','bdca']


w = ['a','b','c','bca','bda','bdca']
# w = ['a','b','ab','xy']

print longest_chain(w_orig)

# print getSmallerWords('abcd')