# Uses python2
import sys

def lcm_naive(a, b):

    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
	
def gcd_new(a,b):
	if a==0:
		return b 
	
	else:
		ma=max(a,b)
		mi=min(a,b)
		return gcd_new(ma%mi,mi)


		
if __name__ == '__main__':
	input = sys.stdin.readline()
	a, b = map(int, input.split())
	gcd=gcd_new(a, b)
	mi=min(a,b)
	ma=max(a,b)
	if ma%mi==0:
		print ma 
	else:
		print mi/gcd*ma

