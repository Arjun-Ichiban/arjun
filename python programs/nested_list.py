
    
    #l = [[name,score] for i in range(int(input())) name=input(),score=float(input()) ]
    #print (l)
if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        l.append([score,name])
    l = sorted(l)
    l1 = []
    a = l[0][0]
    for i in range(1,len(l)-1):
        if(l[i][0]>a):
            for j in range(i,len(l)):
                if(l[i][0]==l[j][0]):
                    l1.append(l[j][1])
            break
    l1 = sorted(l1)
    print(*l1, sep='\n')

    