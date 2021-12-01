# 자연수N 주어짐 => v, 1~N까지의 원소를 갖는 집합의 부분집합을 모두 출력
# 출력순서는 깊이우선탐색, 전위순회방식으로 출력. 공집합은 출력X
import sys

def DFS(v):
    if v == n+1: # 입력값 v보다 커졌을 때
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1 #ch에 v라는 원소를 사용하겠다
        DFS(v+1)
        ch[v] = 0 #ch에 v라는 원소를 사용하지 않겠다
        DFS(v+1)



if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ch = [0]*(n+1) # 원소를 사용할지 안할지 신호주기 위해 check 변수 만듦 // 넉넉하게 n+1개
    DFS(1)
    
    
    
