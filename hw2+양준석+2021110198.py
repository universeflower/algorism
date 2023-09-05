def fload():
     INF = int(1e9) 
 
     print("노드의 개수, 간선의 개수를 입력")
     n, m = map(int, input().split())
     graph = [[INF]*(n+1) for _ in range(n+1)]
     for a in range(1, n+1):
       for b in range(1,n+1):
         if a==b:
             graph[a][b] = 0
             
     for _ in range(m):
         print("A에서 B로 가는 비용은 C 입력")
         a,b,c = map(int, input().split())
         graph[a][b] = c
         
     for k in range(1, n+1):
         for a in range(1, n+1):
             for b in range(1, n+1):
                 graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
                 
     for a in range(1, n+1):
         for b in range(1, n+1):
 
             if graph[a][b] == INF :
                 print("X", end =" ")
             else: 
                 print(graph[a][b], end=" ")
         print()
     print("최단경로 a -> b 입력하시오")
     n, m = map(int, input().split()) 
     print(graph[n][m])
def matrix():
     import sys
     input = sys.stdin.readline
     print("행렬의 개수")
     n = int(input())
     print("행령의 크기를 행 열 순으로 입력")
     a = [list(map(int,input().split())) for i in range(n)]
     d = [[0 for i in range(n)] for i in range(n)]
     
     for i in range(n-1):
         d[i][i+1] = a[i][0]*a[i+1][0]*a[i+1][1]
         
     def dp(start,end):
         if d[start][end] != 0:
             return d[start][end]
         if start == end:
             return 0
         r = float('inf')
         for i in range(start,end):
             temp = dp(start,i) + dp(i+1,end) + a[start][0]*a[i+1][0]*a[end][1]
             if r > temp:
                 r = temp
         d[start][end] = r
         return r
     print(dp(0,n-1))
while True:
         number = int((input("matrix? ->1 , floyd? ->2 what???")))
         if number ==1:
             matrix()
             print("그만 두시겠습니까? y->1 n->0")
             a=input()
             if int(a)==1:
                 break
         elif number ==2:
             fload()
             print("그만 두시겠습니까? y->1 n->0")
             a=input()
             if int(a)==1:
                 break
         else:
             print("다시 입력해주세요")
