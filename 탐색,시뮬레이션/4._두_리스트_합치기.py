import sys

input = sys.stdin.readline
n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

p1 = p2 = 0 # 어디 도는지 표시하는 포인터
c=[]

while p1<n and p2<m: # p1과 p2가 n, m번째까지 돌면 끝남 (한 포인트가 하나의 자료를 끝까지 처리했을 때 끝)
    if a_list[p1] <= b_list[p2]:
        c.append(a_list[p1])
        p1+=1
    else:
        c.append(b_list[p2])
        p2+=1
if p1<n:
    c = c + a_list[p1:]
if p2<m:
    c = c + b_list[p2:]
    
for x in c:
    print(x, end=' ')