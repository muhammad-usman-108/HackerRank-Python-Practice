def average(array):
    # your code goes here
    new_array = []
    for i in array:
        if i not in new_array:
            new_array.append(i)
    return (sum(new_array)/len(new_array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)