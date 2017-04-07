# Uses python2
import sys

def get_fibonacci_huge_new(n, m):
    if n <= 1:
        return n
    else:
		new_list=[0,1]

		if m==2:
			number=3
		elif m==3:
			number=8
		elif (m>3):
			number=2*m
			
		for i in range(2,n%number+1):
			new_list.append(new_list[i-1]+new_list[i-2])
			
		return new_list[-1] % m
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m	


if __name__ == '__main__':
	input = sys.stdin.readline();
	n, m = map(int, input.split())
	#print get_fibonacci_huge_naive(n, m)
	print get_fibonacci_huge_new(n, m)
