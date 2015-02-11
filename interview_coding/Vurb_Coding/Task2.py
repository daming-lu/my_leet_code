__author__ = 'daming'
# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def getOrientation(p, q, r):
    val = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
    if val == 0:
        return 0 # colinear
    if val>0:
        return 1 # clockwise
    return -1 # counter-clockwise

def onSegment(start, mid, end):
    if mid[0]<=max(start[0],end[0]) and mid[0]>=min(start[0],end[0]) \
        and mid[1]<=max(start[1],end[1]) and mid[1]>=min(start[1],end[1]):
        return True
    return False

def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 2.7
    p1 = (K,L)
    q1 = (M,N)

    p2 = (P,Q)
    q2 = (R,S)

    o1 = getOrientation(p1,q1,p2)
    o2 = getOrientation(p1,q1,q2)
    o3 = getOrientation(p2,q2,p1)
    o4 = getOrientation(p2,q2,q1)

    if o1!=o2 and o3!=o4:
        return True

    if o1 == 0 and onSegment(p1, p2, q1):
        return True

    if o2 == 0 and onSegment(p1, q2, q1):
        return True

    if o3 == 0 and onSegment(p2, p1, q2):
        return True

    if o4 == 0 and onSegment(p2, q1, q2):
        return True
    return False

print solution(0,1,4,3,1,3,2,1)
print solution(0,1,4,3,3,2,5,1)

print solution(0,0,1,1,1,-1,-1,1)

print solution(1,-1,-1,1,0,0,1,1)

print solution(0.1,0.1,1,1,1,-1,-1,1)

print solution(0.1,0.1,0.1,1,-0.1,0.1,-0.1,1)

print solution(0.1,0.1,0.1,1,-0.1,0.1,-0.1,1)