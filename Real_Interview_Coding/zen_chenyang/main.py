__author__ = 'daming'

def longest_chain(w):
    my_hash = {}
    for i in range(0, len(w)):
        if len(w[i]) in my_hash:
            my_hash[len(w[i])].append(w[i])
        else:
            my_hash[len(w(i))] = []
            my_hash[len(w[i])].append(w[i])

    print my_hash

w = ['a','b','ba','bca','bda','bdca']
longest_chain(w)