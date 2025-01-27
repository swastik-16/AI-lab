def linear(List,n):
    for i in range(len(List)): 
        if List[i] == n: 
            print("Element found at index ", i)
            break
    print("Element not found")
  
def binary_search(List, x):
    low = 0
    high = len(List) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if List[mid] < x:
            low = mid + 1
        elif List[mid] > x:
            high = mid - 1
        else:
            print("Element found at ", mid)
    print("Element not found")