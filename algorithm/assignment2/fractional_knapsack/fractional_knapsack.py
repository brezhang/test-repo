# Uses python2
import sys

def get_optimal_value(capacity, weights, values):
    ratio=[]
    for i in range(len(weights)):
        ratio.append(values[i]*1.0/weights[i]*1.0)
    value=0
    mid=0
    loc=int
    ratio_2=list(ratio)
    ratio_1=[]
    order=[i for i in range(len(ratio))]
    while ratio_1!=ratio_2:
        ratio_1=list(ratio_2)
        for i in range(len(ratio_2)-1):
            if ratio_2[i]>ratio_2[i+1]:
                mid=ratio_2[i]
                loc=order[i]
                ratio_2[i]=ratio_2[i+1]
                order[i]=order[i+1]
                ratio_2[i+1]=mid
                order[i+1]=loc
    #print order
    #print ratio_2 ,ratio_1,order,ratio
    for i in reversed(order):
        #print i
        if capacity>=weights[i]:
            capacity=capacity-weights[i]
            value=value+values[i]
        else:
            value=value+ min(capacity,weights[i])*ratio[i]
            break

    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
