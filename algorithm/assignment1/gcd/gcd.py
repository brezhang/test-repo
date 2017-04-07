# Uses python2
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
def gcd_new(a,b):
	if a==0:
		print b 
	else:
		ma=max(a,b)
		mi=min(a,b)
		gcd_new(ma%mi,mi)

	
if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    gcd_new(a, b)
