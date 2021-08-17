"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def part(arr, low, high):
	i = (low-1)
	pivot = arr[high]   
	for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
		if arr[j] <= pivot:
  
            
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)


def sort(arr, l ,h):
	if len(arr) == 1:
		return arr
	if l<h:
		p = part(arr, l , h)
		sort(arr, l , p-1)
		sort(arr,p,h)

def quicksort(array):
	# Your code goes here
	n = len(array)
	sort(array, 0 , n-1)
	return array