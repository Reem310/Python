def Countdown(num):
    arr = []
    for x in range(num, -1, -1):
        arr.append(x)
    return arr
print(Countdown(5))


arr=[]
def print_and_return(arr):
    print(arr[0])
    return arr[1]
print_and_return([1,2])


arr=[]
def first_plus_length(arr):
    sum = arr[0]+len(arr)
    return sum
print(first_plus_length([1,2,3,4,5]))


arr2=[]
def values_greater_than_second(arr):
    for x in range(0,len(arr),1):
        if  len(arr)<2:
            return False
        elif arr[x]>arr[1]:
            arr2.append(arr[x])
    print(len(arr2))
    return arr2  
print(values_greater_than_second([5,2,3,2,1,4]))   
print(values_greater_than_second([5]))


def length_and_value(a,b):
    arr=[]
    for x in range(a):
        arr.append(b)
    return arr

print(length_and_value(4,7))
print(length_and_value(6,2))