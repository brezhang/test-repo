# Uses python2
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
		return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10
def fibonacci_sum(n):
	sum=1
	if n <= 1:
		sum=n
	else:
		new_list=[0,1]
		for i in range(2,n+1):
			new_list.append(new_list[i-1]+new_list[i-2])
			sum=(sum %10 +new_list[i] %10 ) %10

	return sum% 10	
if __name__ == '__main__':
	input = sys.stdin.readline()
	n = int(input)
	#print str(fibonacci_sum_naive(n)) +'old'
	print fibonacci_sum(n)
