# Uses python2
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #print left,right,'before left and right index'
    left_m = get_majority_element(a, left, (left + right - 1)//2 + 1)
    right_m = get_majority_element(a, (left + right - 1)//2 + 1, right)
    #print left_m, a ,left, (left + right - 1)//2 + 1,'left'
    #print right_m,a, (left + right - 1)//2 + 1, right,'right'

    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    #print right,left, left_count, 'im left_count'
    if left_count > (right-left)//2:
        #print left_count,'true'
        return left_m

    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right-left)//2:
        #print right_count,'right true'
        return right_m

    return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n=data[0]
    a=data[1:]
    #print n,a
    if get_majority_element(a, 0, len(a))!=-1:
        print 1
    else:
        print 0

