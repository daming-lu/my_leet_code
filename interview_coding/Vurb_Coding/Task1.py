__author__ = 'daming'

def doSum(a,b,carry):
    result = ord(a)-ord('0')+ord(b)-ord('0')+ord(carry)-ord('0')
    result = int(result)
    carry = result/10
    result = result%10
    return (str(result),str(carry))

def addTwoStrings(a, b):
    a = a[::-1]
    b = b[::-1]
    min_len = min(len(a), len(b))
    carry = '0'

    final_result = ""
    i = 0
    while i<min_len:
        cur_a = a[i]
        cur_b = b[i]
        (result, carry) = doSum(cur_a, cur_b, carry)
        final_result+=result
        i+=1
    while i<len(a):
        cur_a = a[i]
        (result, carry) = doSum(cur_a, "0", carry)
        final_result+=result
        i+=1
    while i<len(b):
        cur_b = b[i]
        (result, carry) = doSum("0", cur_b, carry)
        final_result+=result
        i+=1

    while carry!="0":
        (result, carry) = doSum("0", "0", carry)
        final_result+=result

    return final_result[::-1]

def multiElevens(N):
    last_result = "11"
    while N>1:
        last_result = addTwoStrings(last_result, last_result+"0")
        N-=1
    return last_result

def solution(N):
    if N==0:
        return 1
    product = multiElevens(N)
    return sum([1 for x in product if x=='1'])

# print addTwoStrings("123","123123")
print solution(6)

