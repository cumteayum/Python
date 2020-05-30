lambda selectionSort:

	for i in range(len(arr)):
		minimum = 1

		for j in range (i + 1, len(arr)):
			if arr[j] < arr[minimum]:
				minimum = j

		arr[minimum], arr[i] = arr[i], arr[minimum]

		return arr

arr = [2,4,7,5,8,3]
selectedarr = selectionSort(arr)
print(selectedarr)