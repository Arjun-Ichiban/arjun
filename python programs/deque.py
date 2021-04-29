from collections import deque
if __name__ == '__main__':
    d = deque()
    n = int(input())
    for i in range(n):
        s = input()
        l = list(s.split())
        if l[0]=='append':
            d.append(l[1])
            print (d)
        elif l[0]=='appendleft':
            d.appendleft(l[1])
            print (d)
        elif l[0]=='pop':
            d.pop()
            print (d)
        elif l[0]=='popleft':
            d.popleft()
            print (d)
    
    list(d)
    print(*d)
