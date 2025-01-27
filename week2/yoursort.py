def bubble(arr):
    n = len(arr)  
    for i in range(n):
        for j in range(0, n-i-1):  
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]
def selection(arr):
    length = len(arr)  
    for i in range(length-1):   
        minIndex = i  
        for j in range(i+1, length):  
            if arr[j]<arr[minIndex]:  
                minIndex = j  
        arr[i], arr[minIndex] = arr[minIndex], arr[i] 
def insertion(arr):
    n = len(arr)  
    if n <= 1:
        return 
    for i in range(1, n):
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = key

