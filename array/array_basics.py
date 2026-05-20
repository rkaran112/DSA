#in python the array element references are storen in contigious location instead of the elments
arr = [0,1,2,3,4]
element = 5
arr.append(None)
n = len(arr)
#insertion 

# at beggining 
# for i in range(n-1,-1,-1):
#      arr[i+1]= arr[i]
# arr[0] = element
# print(arr)

# #middle 
# pos = 2
# for i in range(n-1,pos-1,-1):
#     arr[i] = arr[i-1]
# arr[pos-1] = element
# print(arr)

# arr[n] =element

# #end
# for i in range(n+1):
#     print(arr)

## Deletion

#begining
for i in range(n):
    arr[i-1] = arr[i]
print(arr)

pos=2
#middle 
for i in range(pos,n):
    arr[i-1] = arr[i]