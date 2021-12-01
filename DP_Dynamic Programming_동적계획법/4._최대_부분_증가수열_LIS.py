import sys
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0) # 앞에 0을 넣어서 리스트의 1번 인덱스부터 시작하게 함 (인덱스 0 무시하도록 1칸 뒤로 미룸)

dy = [0]*(n+1)
dy[1] = 1
res = 0 # 최대 길이

for i in range(2, n+1):
    max = 0 
    for j in range(i-1, 0, -1): # i앞항부터 1번까지 -1씩
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j] # dj[j] = arr[j]값이 마지막항인 증가수열의 최대 길이
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]
print(res)