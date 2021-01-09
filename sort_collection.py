class mySort:

	def __repr__(self):
		return '''Choose sorting category:
	1. Insertion sort
	2. Selection sort
	3. Exchange sort
	4. Merge sort
	5. Distribution sort
	6. Tim
	'''


class Insertion(mySort):
	
	def __repr__(self):
		return '''Insertion sort category:
	1. direct insertion sort
	2. binary insertion sort
	3. shell sort
	'''

	def direct_insertion_sort(nums):
		for i, key in enumerate(nums):
			j = i
			while j > 0 and nums[j-1] > key:
				nums[j] = nums[j-1]
				j -= 1
			nums[j] = key
			print(f"Current array is: {nums}")
		return nums

	def binary_insertion_sort(nums):
		for i, key in enumerate(nums):
			left, right = 0, i - 1
			while left <= right:
				mid = left + (right - left) // 2
				if key > nums[mid]:
					left = mid + 1
				else:
					right = mid - 1
			for j in range(i, left, -1):
				nums[j] = nums[j - 1]
			nums[left] = key
			print(f"Current array is: {nums}")
		return nums

	def shell_sort(nums):
		gap = len(nums) // 2
		while gap:
			for i in range(gap, len(nums)):
				key = nums[i]
				j = i
				while j >= gap and nums[j - gap] > key:
					nums[j] = nums[j - gap]
					j -= gap
				nums[j] = key
			gap //= 2
			print(f"Current array is: {nums}")
		return nums


class Selection(mySort):
	
	def __repr__(self):
		return '''Selection sort category:
	1. direct selection sort
	2. heap sort
	'''

	def direct_selection_sort(nums):
		for i in range(len(nums)):
			min_idx = i
			for j in range(i + 1, len(nums)):
				if nums[j] < nums[min_idx]:
					min_idx = j
			nums[i], nums[min_idx] = nums[min_idx], nums[i]
			print(f"Current array is: {nums}")
		return nums

	def heap_sort(nums):
	
		# adjust curr position to satisfy heap property
		def max_heapify(curr, heap_size):
			largest = curr
			left = 2 * curr + 1
			right = 2 * curr + 2

			if left < heap_size and nums[curr] < nums[left]:
				largest = left
			if right < heap_size and nums[largest] < nums[right]:
				largest = right
			if largest != curr:
				nums[curr], nums[largest] = nums[largest], nums[curr]
				max_heapify(largest, heap_size)

		# buildup maxheap
		n = len(nums)
		for i in range(n // 2 - 1, -1, -1):
			max_heapify(i, n)

		# select element and heapify after swap
		for i in range(n - 1, 0, -1):
			nums[i], nums[0] = nums[0], nums[i]
			max_heapify(0, i)
			print(f"Current array is: {nums}")
		return nums


class Exchange(mySort):

	def __repr__(self):
		return '''Exchange sort category:
	1. bubble sort
	2. cocktail sort
	3. quick sort
	'''

	def bubble_sort(nums):
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] > nums[j]:
					nums[i], nums[j] = nums[j], nums[i]
			print(f"Current array is: {nums}")
		return nums

	def cocktail_sort(nums):
		shift = 0
		left, right = 0, len(nums) - 1
		while left < right:
			for i in range(left, right):
				if nums[i] > nums[i + 1]:
					nums[i], nums[i + 1] = nums[i + 1], nums[i]
					shift = i
			right = shift
			for i in range(right, left, -1):
				if nums[i] < nums[i - 1]:
					nums[i], nums[i - 1] = nums[i - 1], nums[i]
					shift = i
			left = shift
			print(f"Current array is: {nums}")
		return nums

	def quick_sort(nums):

		def divide_conquer(left, right):
			i, j = left, right
			pivot = nums[left]
			while i < j:
				while i < j and nums[j] >= pivot:
					j -= 1
				if i < j:
					nums[i], nums[j] = nums[j], nums[i]
				while i < j and nums[i] <= pivot:
					i += 1
				if i < j:
					nums[i], nums[j] = nums[j], nums[i]
				print(f"Current array is: {nums}")
			if i != left:
				divide_conquer(left, i - 1)
			if j != right:
				divide_conquer(j + 1, right)

		divide_conquer(0, len(nums)-1)
		return nums
		
	def quick_sort_mid(nums):
		
		def divide_conquer(left, right):
			if (right - left) < 1: return
			pivot = nums[(left + (right - left) // 2)]
			i, j = left, right
			while i <= j:
				while nums[i] < pivot:
					i += 1
				while nums[j] > pivot:
					j -= 1
				if i <= j:
					nums[i], nums[j] = nums[j], nums[i]
					i += 1; j -= 1
			divide_conquer(left, j)
			divide_conquer(i, right)

		divide_conquer(0, len(nums)-1)
		return nums
	

class Merge(mySort):

	def __repr__(self):
		return '''Merge sort category:
	1. top-down
	2. bottom-up
	'''

	def merge(left, right):
		result = []
		while left and right:
			if left[0] <= right[0]:
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		return result + left + right


	def top_down(nums):
		print(f"Current array is: {nums}")
		if len(nums) < 2:
			return nums
		mid = len(nums) // 2
		left = Merge.top_down(nums[:mid])
		right = Merge.top_down(nums[mid:])
		return Merge.merge(left, right)


	def bottom_up(nums):
		if len(nums) < 2:
			return nums
		queue = list([num] for num in nums)
		while len(queue) > 1:
			print(f"Current array is: {queue}")
			left = queue.pop(0)
			right = queue.pop(0)
			queue.append(Merge.merge(left, right))
		return queue.pop()


class Distribution(mySort):

	def __repr__(self):
		return '''Distibution sort category:
	1. counting sort
	2. bucket sort
	3. radix sort
	'''

	def counting_sort(nums):
		mini, maxi = min(nums), max(nums)
		range_of_elements = maxi - mini + 1
		count = [0 for _ in range(range_of_elements)]
		output = [0 for _ in range(len(nums))]

		# Make array element counter
		for i in range(len(nums)):
			count[nums[i] - mini] += 1
			
		# Use count to make location mapping
		for i in range(1, len(count)):
			count[i] += count[i-1]
		
		# Counter now maps array element location
		for i in range(len(nums)-1, -1, -1):
			count[nums[i] - mini] -= 1
			output[count[nums[i] - mini]] = nums[i]
		return output


	def bucket_sort(nums, bucket_size=10):
		mini, maxi = min(nums), max(nums)
		bucket_num = (maxi - mini) // bucket_size + 1
		buckets = [[] for i in range(bucket_num)]

		# Put array elements in different buckets
		for num in nums:
			idx = (num - mini) // bucket_size
			buckets[idx].append(num)

		# Sort individual buckets
		for i in range(bucket_num):
			buckets[i].sort()

		# concatenate the result
		k = 0
		for i in range(bucket_num):
			for j in range(len(buckets[i])):
				nums[k] = buckets[i][j]
				k += 1
		return nums


	def radix_sort(nums):
		radix = 10
		maxi = max(nums)
		exp = 1
		while maxi // exp > 0:
			Distribution.bucket_sort(nums, exp)
			exp *= radix
		return nums
		

class Tim(mySort):

	def __repr__(self):
		return '''Tim:
	1. Tim sort
	'''

	def tim_sort(nums):

		def insertion_sort(nums, left=0, right=None):
			for i in range(left, right):
				key = nums[i]
				j = i
				while j > left and nums[j - 1] > key:
					nums[j] = nums[j - 1]
					j -= 1
				nums[j] = key
			return nums

		min_run = 32
		n = len(nums)
		for i in range(0, n, min_run):
			right_bound = min((i + min_run), n)
			insertion_sort(nums, i, right_bound)

		size = min_run
		while size < n:
			for start in range(0, n, size * 2):
				mid = start + size
				end = min((start + size * 2), n)
				left = nums[start: mid]
				right = nums[mid: end]
				merged_array = Merge.merge(left, right)
				nums[start: start + len(merged_array)] = merged_array
				print(f"Current array is: {nums}")
			size *= 2
		return nums


if __name__ == "__main__":
	
	categories = {
		'1': Insertion,
		'2': Selection,
		'3': Exchange,
		'4': Merge,
		'5': Distribution,
		'6': Tim
	}

	methods = {
		Insertion: {
			'1': 'direct_insertion_sort',
			'2': 'binary_insertion_sort',
			'3': 'shell_sort'
		},
		Selection: {
			'1': 'direct_selection_sort',
			'2': 'heap_sort'
		},
		Exchange: {
			'1': 'bubble_sort',
			'2': 'cocktail_sort',
			'3': 'quick_sort',
		},
		Merge: {
			'1': 'top_down',
			'2': 'bottom_up'
		},
		Distribution: {
			'1': 'counting_sort',
			'2': 'bucket_sort',
			'3': 'radix_sort'
		},
		Tim: {
			'1': 'tim_sort'
		}
	}

	import random
	nums = list(range(100))
	random.shuffle(nums)

	user_category = input("{}\n".format(mySort()))
	category = categories[user_category]
	user_method = input("{}\n".format(category()))
	method = getattr(category, methods[category][user_method])
	print("The original array is: {}".format(nums))
	print("The sorting result is: {}".format(method(nums)))

