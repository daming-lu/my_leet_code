__author__ = 'daming'

import sys
import os
import fileinput

def workhorse(step, ans_so_far, num, ans, marks, target, found_rank):
    if len(found_rank)>0:
        return
    if step == len(num):
        if "".join(ans_so_far) == target:
            found_rank.append((True, len(ans)))
            return
        ans.append(list(ans_so_far))
        return
    for i in range(0, len(num)):
        if not marks[i]:
            if i>0 and num[i] == num[i-1] and marks[i-1] == False:
                continue
            marks[i] = True
            ans_so_far.append(num[i])
            workhorse(step+1, ans_so_far, num, ans, marks, target, found_rank)
            ans_so_far.pop()
            marks[i] = False

def get_rank(word):
    target = word
    word = "".join(sorted(word))
    ans = []
    marks = [False for w in word]
    found_rank = []
    workhorse(0, [], word, ans, marks, target, found_rank)
    return found_rank[0][1]

def get_ranks(words):
    ans = []
    for word in words:
        ans.append(get_rank(word))
    return ans

_words = []
count = 0
_words_cnt = 0
_words_i = 0
for line in fileinput.input():
    if count == 0:
        _words_cnt = int(line.strip())
        _words_i=0
        count += 1
        continue
    else:
        if _words_i < _words_cnt:
            _words_item = line
            _words_item = _words_item.strip().rstrip()
            _words.append(_words_item)
            _words_i+=1

# print _words
res = get_ranks(_words)
for res_cur in res:
    print str(res_cur), "\n"

"""
f = open(os.environ['OUTPUT_PATH'], 'w')


_words_cnt = int(raw_input())
_words_i=0
_words = []
while _words_i < _words_cnt:
    _words_item = raw_input()
    _words.append(_words_item)
    _words_i+=1


res = get_ranks(_words)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()
"""