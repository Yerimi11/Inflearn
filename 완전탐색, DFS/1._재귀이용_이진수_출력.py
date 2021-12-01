# 10진수 N이 입력되면 2진수로 변환하여 출력 (재귀함수 사용)
import sys

def DFS(x):
    if x == 0:
        return # 함수를 종료시켜라
    
    else:
        DFS(x//2)
        print(x%2, end=' ')


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    DFS(n)
