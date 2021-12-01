import sys
n = int(sys.stdin.readline())

# dy : 다이나믹 테이블 ㅎㅎ
dy = [0] * (n+1) # 1차원 배열 (리스트 만들기) / n+1인 이유 : 인덱스 0은 버리려고
# 1, 2의 값 처럼 직관적으로 알 수 있는 것은 바로 기록을 해주고 시작한다
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])