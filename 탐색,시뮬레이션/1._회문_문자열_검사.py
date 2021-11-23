#회문 문자열 : 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우 
import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = input()
    s = s.upper()
    size=len(s)
    for j in range(size//2):
        #맨 첫글자와 맨 뒷글자가 같지 않으면(회문이 아니면)
        if s[j]!=s[-1-j]:
            print("#%d NO %(i+1)")
            break
    else:
        print("#d YES" %(i+1))


    # #더 간단하게
    #         #s를 reverse
    # if s == s[::-1]:
    #     print("#%d YES" %(i+1))
    # else:
    #     print("#%d NO" %(i+1))