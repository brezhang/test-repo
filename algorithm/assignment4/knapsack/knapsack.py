# Uses python3

import sys


def zeros(rows, cols):
    row = []
    data = []
    for i in range(cols):
        row.append(0)
    for i in range(rows):
        data.append(row[:])
    return data


def optimal_weight(W, w, n):
    c = [0] * (W+1)
    for i in range(len(w)):
        #for j in range(W,0,-1):
        for j in range(W, w[i]-1, -1):
            print (j)
            c[j] = max(c[j], c[j - w[i]] + w[i])
    return c[W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
