arr=raw_input()
def smallest(arr,s):
    min=arr[0]
    for i in range(1, s):
        if arr[i]<min:
             min=arr[i]
    return min
n=len(arr)
ans=smallest(arr,s)
print ans
