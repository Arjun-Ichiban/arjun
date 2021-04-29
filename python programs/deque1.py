from collections import deque
if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        ans = "Yes"
        m = int(input())
        d = deque(list(map(int,input().split())))
        a = d.pop()
        b = d.popleft()
        if a>b:
            c = a
            d.appendleft(b)
        else:
            c = b
            d.append(a)
        for j in range(m-2):
            a = d.pop()
            b = d.popleft()
            if(a<=c):
                d.appendleft(b)
                c = a
                continue
            elif(b<=c):
                d.append(a)
                c = b
                continue
            else:
                ans = "No"
                break
        if(ans=="Yes" and d.pop()>c):
            ans = "No"
        l.append(ans)
    print(*l) 