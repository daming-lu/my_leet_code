# this is actually 2nd Phone Coding of LinkedIn
def workhorse(inList, ans_so_far, ans):
    if len(inList) == 0:
        # print ans_so_far
        ans.append(list(ans_so_far)) # important
        return

    for i in range(0, len(inList)):
        ans_so_far.append(inList[i])
        removed = inList[i]
        del inList[i]
        workhorse(inList, ans_so_far, ans)
        inList.insert(i,removed)
        ans_so_far.pop()


def permutation(inList):
    ans = []
    workhorse(inList, [], ans)
    return ans


print permutation([1, 2, 3])