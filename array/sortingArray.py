class Sorting:
    def bubbleSort(self,arr):
        n= len(arr)
        for i in range(n-1):
            for j in range(n-i-1): #start swapping from first and last index 
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]= arr[j+1],arr[j]
        return arr
    
    def insertionSort(self,arr):
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j -=1
            arr[j+1] = key
        return arr
sort = Sorting()
print(sort.bubbleSort([3,2,4,5,1]))
print(sort.insertionSort([3,2,4,5,1]))