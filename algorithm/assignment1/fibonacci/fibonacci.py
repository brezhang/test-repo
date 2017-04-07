# Uses python2
def calc_fib(n):
	if n<=1:
		return n
	else:
		new_list=[0,1]
		for i in range(2,n+1):
			new_list.append(new_list[i-1]+new_list[i-2])
		return new_list[-1]
		
n = int(input())
print calc_fib(n)
