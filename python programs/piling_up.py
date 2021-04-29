if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        ans = 'Yes'
        m = int(input())
        li = list(map(int,input().split()))
        if(li[0]>li[m-1]):
            c = li[0]
            li.pop(0)
        else:
            c = li[m-1]
            li.pop(m-1)
        for j in range(m-2,-1,-1):
            if(li[0]>li[j]):
                if(li[0]<=c):
                    c = li.pop(0)
                elif(li[j]<=c):
                    c = li.pop(j)
                else:
                    ans = 'No'
                    break
            else:
                if(li[j]<=c):
                    c = li.pop(j)
                elif(li[0]<=c):
                    c = li.pop(0)
                else:
                    ans = 'No'
                    break
        l.append(ans)
    print(*l,sep="\n")
            
                

                
        