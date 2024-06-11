<<<<<<< Updated upstream
import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Haider")
    while True:
        s=input("Enter what you want me to speak : ")
        if s=="Bye":
           os.system("say'Have a nice day friend, Bye'")
           break
        command=f"say={s}"
        os.system(command)
=======
print("Program for binary search")
def binary_search(arr,target)
    low=0
    high=len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif low < target:
            low = mid+1
        else :
            high = mid-1
    return -1
no_of_elements=int(input("Enter the no of elements"))
arr=[]
print("Enter the elements")
for i in range (no_of_elements):
    elements=int(input())
    arr.append(elements)
result=binary_search(arr,target)
target=int(input("Enter the target element"))
if result!=-1:
    print ("The target element is found at the index" , result)
else :
    print ("The target element is not found")
>>>>>>> Stashed changes
