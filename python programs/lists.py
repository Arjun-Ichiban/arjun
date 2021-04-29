if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        l1 = list(input())
        if(l1[0]=='insert'):
            l.insert(int(l1[1]),int(l1[2]))
        elif(l1[0]=='print'):
            print(l)
        elif(l11[0]=='remove'):
            l.remove(int(l1[1]))
        elif(l1[0]=='append'):
            l.append(int(l1[1]))
        elif(l1[0]=='sort'):
            l.sort()
        elif(l1[0]=='pop'):
            l.pop(int(l1[1]))
        elif(l1[0]=='reverse'):
            l.reverse()
            