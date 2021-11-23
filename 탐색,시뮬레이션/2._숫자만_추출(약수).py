#문자 숫자 섞인 문자열 중에서 숫자열만 추출(자연수) 
#만들어진 자연수와 그 자연수의 약수 개수 출력(앞에 0 이 먼저 나오면 무시)
#입력값 : g0en2Ts8eSoft // 출력 : 28 \n 6 \n
import sys

s = sys.stdin.readline() #g0en2Ts8eSoft 입력받음
res = 0

for x in s: 
    if x.isdecimal(): #x가 0~9까지 숫자일때
        res = res*10+int(x) #첫자리 0은 계산해도 0나와서 무시 됨 
print(res) # 2+8 저장돼서 res의 출력값은 28.

#res의 약수의 개수
cnt=0       #약수는 1부터고, 자기자신 수(res)도 있어야하니까 res+1
for i in range(1, res+1):
        if res % i == 0:
            cnt+=1
print(cnt)
