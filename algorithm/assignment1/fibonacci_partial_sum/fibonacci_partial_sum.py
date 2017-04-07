# Uses python2
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_partial_sum_new(from_,to):
	sum=0
	new_list=[0,1]
	if to<=1:
		return to
	elif (to==2 and from_==1):
		return 2
	elif (to==2 and from_==0):
		return 4
		
	else:
		for i in range(2,to+1):
			new_list.append(new_list[i-1]+new_list[i-2])
			if i>=from_:
				
				sum=(sum+new_list[i] % 10 ) %10

	return sum%10

if __name__ == '__main__':
	input = sys.stdin.readline();
	from_, to = map(int, input.split())
	#print str(fibonacci_partial_sum_naive(from_, to))+"old"
	print fibonacci_partial_sum_new(from_,to)
