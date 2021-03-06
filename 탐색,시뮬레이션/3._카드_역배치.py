# 1~20까지의 숫자카드 쭈루룩 오름차순으로 있는데 그 사이에서 특정 구간의 카드를 역순으로 놓음
# 바뀐 상태에서 구간이 또 주어지면 그 구간을 또 역순으로 배치. 
# 10개의 구간이 주어졌을 때 순서대로 재배치한 후 마지막 카드들의 배치를 구하라
# 입력 - i번째 줄에 i번째 구간의 시작위치 ai, 끝위치 bi
import sys

# 1~20까지
a = list(range(21))

for _ in range(10):
    s, e = map(int, sys.stdin.readline().split())
    # 1~9 리스트에서 2~7구간을 역순으로 자리바꾸려면 2,7 바꾸고 3,6 바꾸고 4,5 이렇게 세 번 바꾸면 됨 0> n번?구간(7-2)+1//2해준다 
    for i in range((e-s+1)//2):
        # 자리 스와프
        a[s+i], a[e-i] = a[e-i], a[s+i] #a의 시작지점s+i, 뒤쪽e는 앞으로 하나씩 와야하니까 e-i

a.pop(0) # 맨 앞에 0 출력되는거 빼버림
for x in a:
    print(x, end=' ') #옆으로 출력
    
        