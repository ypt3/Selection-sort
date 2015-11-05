arr = []

import random

for i in range(0, 11):	
	arr.append(random.randint(1,100))


# def swap_sort(arr_list, index1, index2):
# 	temp = arr_list[index2]
# 	arr_list[index2] = arr_list[index1]
# 	arr_list[index1] = temp



# def selection_sort(arr):
# 	#loop entire array
# 	for i in range(0, len(arr)):
# 		# find the position has the smallest number
# 		#start with current location
# 		current_i = i
# 		for j in range(i+1, len(arr)):
# 			if arr[j] < arr[current_i]:
# 				current_i = j
# 		temp = arr[current_i]
# 		arr[current_i] = arr[i]
# 		arr[i] = temp
		
# 		# swap_sort(arr, current_i, i)
# 		print arr

# selection_sort(arr)



def selection_sort(arr):
	for i in range(0, len(arr)):
		min_i = i
		max_i = i

		for j in range(i, len(arr)):
			if arr[j] < arr[min_i]:
				min_i = j
		for k in range(i, len(arr)):
			if arr[k] > arr[max_i]:
				max_i = k

		(arr[min_i], arr[i]) = (arr[i], arr[min_i])
		(arr[max_i], arr[len(arr)-1]) = (arr[len(arr)-1], arr[max_i])


		# temp = arr[max_i]
		# arr[max_i] = arr[len(arr)-1]
		# arr[len(arr)-1] = temp

		print arr
selection_sort(arr)









