print("Program for binary search")
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[low] < target:
            low = mid+1
        else :
            high = mid-1
    return -1
no_of_elements=int(input("Enter the no of elements : "))
arr=[]
print("Enter the elements : ")
for i in range (no_of_elements):
    elements=int(input())
    arr.append(elements)
target=int(input("Enter the target element to be searched : "))
result=binary_search(arr,target)
if result!=-1:
    print ("The target element is found at the index : " , result)
else :
    print ("The target element is not found.")