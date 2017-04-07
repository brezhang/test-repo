# Uses python2
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_new(n):
	if n <= 1:
		return n
	
	else:
		new_list=[0,1]
		for i in range(2,n+1):
			new_list.append(new_list[i-1]%10 +new_list[i-2]%10)
		return new_list[-1] % 10 
		
if __name__ == '__main__':
	input = sys.stdin.readline()
	n = int(input)
	print get_fibonacci_last_digit_new(n)
