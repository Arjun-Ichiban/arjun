if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    # arr = sorted(arr,reverse=True)
    # for i in range(len(arr)):
    #     if(arr[0]!=arr[i]):
    #         print(arr[i])
    #         break
    n = int(input())
    arr = set(map(int, input().split()))
    print (sorted(arr)[-2])