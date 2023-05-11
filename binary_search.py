# Normally for searching an element in the list we use linear searching that is we 
# look throgh the entire list for the element ,and if the element is present we give 
# the output , But this is not practical for a large set of data thats why we use Binary 
# Search


# So, How does this Binary Search work? Well in Binary Search , we first sort the values 
# of the array .Then we fix a upper value and a lower value , we tell the mid-value to be 
# mid . Now, if the mid is smaller than the required value we increase the lower limit to search
# bigger number than mid , if mid is greater than the required value than we decrease the upper bound 
# to search smaller number than the mid .

#Step 1
#Taking Array as input from the user 
import numpy as np 
arr_str = input("Enter the array elements (space-separated): ")
arr = list(map(int, arr_str.split()))
arr_n=np.array(arr)
arr_sort=np.sort(arr_n)
print (arr_sort)

#Step 2
#Now , Lets define a function for the binary search
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid =(u+l)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else :
            if list[mid]<n:
                l=l+1
            elif list[mid]>n:
                u=u-1                


#Now taking the element to search as input and passing it through the function
ele=int(input('What element you want to search for'))
if search(arr_sort, ele):
    print ("The number you are looking for is present at position",pos+1)
else:
    print("element not found")    