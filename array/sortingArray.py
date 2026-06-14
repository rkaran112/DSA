class Sorting:
    def bubbleSort(self,arr):
        n= len(arr)
        for i in range(n-1):
            for j in range(n-i-1): #start swapping from first and last index 
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]= arr[j+1],arr[j]
        return arr
    
    def insertionSort(self,arr):
        first = arr[0]
        n = len(arr)
        for i in range(n-1):
            if first<arr[i+1]:
                    first = arr[i+1]
                    arr[i+1] = first
sort = Sorting()
print(sort.bubbleSort([3,2,4,5,1]))