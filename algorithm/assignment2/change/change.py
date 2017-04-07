# Uses python3
import sys

def get_change(m):
	coins=[10,5,1]
	if w==0:
		return count
	w=m
	while w!=0:
	for i in coins:
		if w>=i:
			w=w-i
			count=count+1
    #write your code here
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
