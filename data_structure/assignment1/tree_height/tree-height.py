# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def __int__(self):
            self.n=0
            self.parent=[]

        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
            self.cache=[0]*self.n

        def path_len(self,node_id):
            parent=self.parent[node_id]
            #print (node_id,parent)
            if parent==-1:
                return 1
            if self.cache[node_id]:
                return self.cache[node_id]
            self.cache[node_id]=1+self.path_len(self.parent[node_id])
            #print (self.cache[node_id])
            return self.cache[node_id]
        def compute_height(self):
            #print ([self.path_len(i) for i in range(self.n)])
            return max([self.path_len(i) for i in range(self.n)])

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
