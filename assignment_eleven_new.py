arr = []

import random
import datetime

for i in range(0, 5):	
	arr.append(random.randint(1,10))
time_start = datetime.datetime.now()

def selection_sort(arr):
	arr_length = len(arr)
	for i in range(arr_length):
		smaller_number_location = i
		# we say i+1 because we don't want to compare number to itself
		for j in range(i+1, arr_length):
			#if THIS number is smaller than THAT number, 
			if arr[j] < arr[smaller_number_location]:
				# Then we consider the location 'j' as the new location of the smaller number
				smaller_number_location = j

		#if smaller_number_location is not equal to the current location of the number being checked in our loop
		if smaller_number_location != i:
			#then store this current number being checked to a temp variable ( we don't want to lose this number )
			temp = arr[i]
			# Whatever this current number is from location i, we replace it with a number (which is smaller) using the smaller_number_location variable as index to the arr variable (to locate the number)
			arr[i] = arr[smaller_number_location]
			# We don't want to lose the number we just overwrite from location i, that's why we need to put the temp number back to wherever the smaller number was stored. It's like we switched the temp with the smaller and vice versa.
			arr[smaller_number_location] = temp
		print arr

selection_sort(arr)
time_end = datetime.datetime.now()
time = time_end - time_start
print time.microseconds
