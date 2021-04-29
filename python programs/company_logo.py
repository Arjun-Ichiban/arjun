if __name__ == '__main__':
    s = input()
    s = sorted(s)
    l = {}
    for i in range(len(s)):
        t = (s[i],s.count(s[i]))
        l.update([t])
    l = [(k, v) for k, v in l.items()]

    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if(l[j][1] < l[j+1][1]):
                t = l[j]
                l[j] = l[j+1]
                l[j+1] = t 

    for i in range(3):
        print(l[i][0],l[i][1])       
