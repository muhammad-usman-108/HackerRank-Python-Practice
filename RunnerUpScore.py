if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    sort=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    max = arr[n-1]
    i=n-1
    while(i>=0):
        if(arr[i]<max):
            max=arr[i]
            break
        i=i-1
    print(max)
