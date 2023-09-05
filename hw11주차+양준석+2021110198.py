def promising(i,weight,total):#true false 판단(bool)
    return (weight + total >= W) and (weight == W or weight + w[i+1] <= W); # 가능성 확인

def s_s(i,weight, total, include):#sumofsubset W에 맞는 경우의 수 찾기
    if promising(i, weight, total):
        if weight == W:
            print(include)
        else:
            include[i+1] = 1
            s_s(i+1, weight+w[i+1], total-w[i+1], include)
            include[i+1] = 0
            s_s(i+1, weight, total-w[i+1], include)

def color(i,vcolor):
    if promising2(i,vcolor): # 맨 처음에는 promising True, 마지막은 i==n-1이 되는 순간 print되서 종료
        if (i==n-1):
            print(vcolor)
        else:
            for j in range(1,m+1):
                vcolor[i+1] = j
                color(i+1, vcolor)

def promising2(i,vcolor): #true false 판단(bool)
    switch = True
    j = 0
    while j<i and switch:
        if W[i][j] and vcolor[i]==vcolor[j]:
            switch = False
        j += 1
        
    return switch

n=5
w=[1,4,5,6,8]
W=10
print("muster  =" , w, "W =", W)
include = n*[0]
total=0
for k in w:
    total += k
s_s(-1,0,total,include)

n=7 #노드 수
W=[[0,1,1,0,0,0,1],[1,0,1,1,0,0,0],[1,1,0,1,1,1,1],[0,1,1,0,1,0,0],[0,0,1,1,0,1,0],[0,0,1,0,1,0,1],[1,0,1,0,0,1,0]] #각 중심 노드 기준 연결노드
vcolor=n*[0]
m=3#색칠 수
print("m-coloring node =",n,"m =",m)
color(-1,vcolor)

    

