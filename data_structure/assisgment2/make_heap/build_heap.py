# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._fastswap = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._fastswap))
        # for swap in self._swaps:
        for swap in self._fastswap:
            print(swap[0], swap[1])

    def Parent(self,i):
      if i%2==0 and i-2>=0:
        r=round((i - 2) / 2)
      elif i%2!=0 and i-1>=0:
        r = round((i - 1) / 2)
      else:
        r=i
      return r

    def SiftUp(self,i):
        maxIndex = i

        r=self.Parent(i)
        if r<= len(self._data) and self._data[r] > self._data[maxIndex]:
            maxIndex = r

        if i != maxIndex:
            self._fastswap.append((i, maxIndex))
            self._data[i], self._data[maxIndex] = self._data[maxIndex], self._data[i]

            self.SiftUp(maxIndex)

    def BuildHeap(self):
        n = len(self._data)
        for i in range(n-1,0,-1):
          self.SiftUp(i)

    def Solve(self):
        self.ReadData()
        self.BuildHeap()
        # self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
