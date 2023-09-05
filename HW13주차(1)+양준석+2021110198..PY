import math
class Heap(object): #힙 클래스.
    n=0
    
    def __init__(self, data):
        self.data=data
    # heap size를 하나 줄여야 함. 인덱스는 1부터 진행
        self.n=len(self.data)-1
        
    def addElt(self,elt): # 요소 추가
        self.n += 1
        self.data.append(elt)
        self.siftUp(self.n)

    def siftUp(self, i): # 맨 마지막 요소를 위로 올림
        while i >= 2:
            j = i // 2 # 부모인덱스
            if self.data[j] >= self.data[i]: # 부모값이 더 크면 종료
                return 
            self.data[j], self.data[i] = self.data[i], self.data[j]
            i = j
                
                
    def siftDown(self,i): #힙 성질을 만족하도록 아래로 내려감.
        siftkey = self.data[i]
        parent = i
        spotfound = False
        while 2*parent <= self.n and not spotfound:
            if 2*parent < self.n and self.data[2*parent] < self.data[2*parent+1]:
                largerchild = 2*parent+1
            else:
                largerchild = 2*parent
            if siftkey < self.data[largerchild]:
                self.data[parent] = self.data[largerchild]
                parent = largerchild
            else:
                spotfound = True
        self.data[parent] = siftkey

    def makeHeap2(self):  #힙 생성
        for i in range(self.n//2,0,-1):
            self.siftDown(i)
     

    def root(self): #힙의 루트요소를 반환

        if(self.n>0):      
        # 추가 하였음. 힙 이 더 이상없을 때는 down 없음
            keyout = self.data[1]
            self.data[1] = self.data[self.n]
            self.n -= 1
            self.siftDown(1)            
            return keyout
    
    def removeKeys(self): # 제힙에서 가장 큰 요소를 제거
        a=[]
        for i in range(self.n):
            a.append(self.root())
        return a
        
    
def heapSort2(a):#힙 정렬을 수행
    h = Heap(a)
    h.makeHeap2()
    return h.removeKeys()

#method1 
a=[0,11,14,2,7,6,3,9,5] # 힙구현에서는인덱스 0을 사용하지 않기에  0 추가    
b = Heap([]) # 인스턴스'b' 생성
print("method 1")
for i in a:
    b.addElt(i)
    print(b.data[1:])

b.addElt(50)
print("METHOD1 ANS",b.data[1:len(b.data)])
print("기본 힙정렬",heapSort2(b.data))

