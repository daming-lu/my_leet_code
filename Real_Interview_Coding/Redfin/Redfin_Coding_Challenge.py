__author__ = 'daming'

import sys
import os

def workhorse(self, step, ans_so_far, num, ans, marks, target, found_rank):
    if found_rank[0][0]:
        return
    if step == len(num):
        if ans_so_far == target:
            found_rank[0][0] = True
            found_rank[0][1] = len(ans)
            return
        ans.append(list(ans_so_far))
        return
    for i in range(0, len(num)):
        if not marks[i]:
            if i>0 and num[i] == num[i-1] and marks[i-1] == False:
                continue
            marks[i] = True
            ans_so_far.append(num[i])
            self.workhorse(step+1, ans_so_far, num, ans, marks)
            ans_so_far.pop()
            marks[i] = False

def get_rank(word):
    target = word
    word.sort()
    ans = []
    marks = [False for w in word]
    found_rank = [(False, -1)]
    workhorse(0, [], word, ans, marks, target, found_rank)
    return found_rank[0][1]

def get_ranks(words):
    ans = []
    for word in words:
        ans.append(get_rank(word))
    return ans


