import sys


if __name__ == "__main__" :
    n = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    dy = [1000] * (m+1)
    dy[0] = 0 # 0원을 거슬러주는데 필요한 동전 갯수는 0개
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j] = min(dy[j], dy[j-coin[i]]+1) # 동전 최소갯수 갱신 (현재 코인 i번째 동전을 사용해서..)
    print(dy[m])