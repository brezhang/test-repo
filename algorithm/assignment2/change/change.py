# Uses python2
import sys

def get_change(m):
	coins=[10,5,1]
	w=m
	count=0
	while w!=0:
		for i in coins:
			if w>=i:
				w=w-i
				count=count+1

	return count

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print get_change(m)
