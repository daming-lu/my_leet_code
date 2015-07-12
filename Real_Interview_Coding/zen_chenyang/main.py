__author__ = 'daming'

def getSmallerWords(word):
    ans = []
    for i in range(0, len(word)):
        ans.append(word[0:i]+word[i+1:])
    return ans

def find_longest(my_hash, length_hash):
    ans = 0
    keys = my_hash.keys()
    # print keys
    for l in keys:
        if l-1 not in my_hash:
            continue
        cur_len_words = my_hash[l]
        for word in cur_len_words:
            words_1_char_less = getSmallerWords(word)
            cur_chain_length = length_hash[word]
            for word_1_char_less in words_1_char_less:
                if word_1_char_less in length_hash:
                    cur_chain_length = max(cur_chain_length, length_hash[word_1_char_less]+1)
            length_hash[word] = cur_chain_length
            if cur_chain_length > ans:
                ans = cur_chain_length
    return ans

def longest_chain(w):
    my_hash = {}
    length_hash = {}
    for i in range(0, len(w)):
        length_hash[w[i]] = 1
        if len(w[i]) in my_hash:
            my_hash[len(w[i])].append(w[i])
        else:
            my_hash[len(w[i])] = list()
            my_hash[len(w[i])].append(w[i])
    ans = find_longest(my_hash, length_hash)

    return  ans

w_orig = ['a','b','ba','bca','bda','bdca']


w = ['a','b','c','bca','bda','bdca']
# w = ['a','b','ab','xy']

print longest_chain(w_orig)

# print getSmallerWords('abcd')