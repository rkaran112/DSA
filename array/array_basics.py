#in python the array element references are storen in contigious location instead of the elments
arr = [0,1,2,3,4]
element = 5
arr.append(None)
n = len(arr)
#insertion 
#At beggining 
for i in range(n-1,-1,-1):
     arr[i+1]= arr[i]
arr[0] = element
print(arr)

# #middle 
pos = 2
for i in range(n-1,pos-1,-1):
    arr[i] = arr[i-1]
arr[pos-1] = element
print(arr)

#end
arr[n] =element
for i in range(n+1):
    print(arr)

## Deletion

#begining
for i in range(n):
    arr[i-1] = arr[i]
print(arr)

pos=2
#middle 
for i in range(pos,n):
    arr[i-1] = arr[i]
    
    
#quick revision of arrays-
#insertion - begining - arr[i] = arr[i-1] -> arr[0]  =ele,middle -arr[i]=arr[i-1] (for i in range(n-1,pos-1,-1))->arr[pos] - ele,last arr[n] = eke
#deletion - begining arr[i-1] = arr[i], middle -for(i in range(pos+1,-1))arr[i-1] = arr[i],Last arr[n]  = None

ele=3
#first occurance-
for i in range(0,n):
    if  arr[i]==ele:
        for j in range(i+1,n):
            arr[j-1] = arr[j]
            
        arr[i-1] = None
        break
i= 0  
while i<n:
    if  arr[i]==ele:
        for j in range(i+1,n):
            arr[j-1] = arr[j]
        
        n=n-1
        arr[n] = None 
