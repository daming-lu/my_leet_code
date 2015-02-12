__author__ = 'daming'
def findNeedleInHaystack(haystack, needle):
    if needle == None:
        return -1
    needle_len = len(needle)
    for i in range(0, len(haystack)-needle_len+1):
        if haystack[i:(i+needle_len)] == needle:
            return i

    return -1

print findNeedleInHaystack("alpha", None)


def kMostFrequent(list, k):
    # (7,3),(3,2),(5,2)

    my_map = {}
    for e in list:
        if e in my_map:
            my_map[e] += 1
        else:
            my_map[e] = 1

    occurance = []
    for key in my_map:
        occurance.append((key, my_map[key]))

    occurance.sort(key=lambda x:x[1])

    ans = []
    i = 0
    while i < k:
        ans.append(occurance[len(occurance)-1-i][0])
        i+=1
    return ans

test1 = [7, 3, 5, 7, 7, 3, 5, 1]

print kMostFrequent(test1, 3)