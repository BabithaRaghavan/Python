# Python3 implementation to print
# the string in Lexicographical order

# Used for index in heap
x = -1;

# Predefining the heap array
heap = [0] * 1000;

# Defining formation of the heap
def heapForm(k):
	global x;
	x += 1;

	heap[x] = k;

	child = x;

	index = x // 2;

	# Iterative heapiFy
	while (index >= 0):

		# Just swapping if the element
		# is smaller than already
		# stored element
		if (heap[index] > heap[child]):

			# Swapping the current index
			# with its child
			tmp = heap[index];
			heap[index] = heap[child];
			heap[child] = tmp;
			child = index;

			# Moving upward in the
			# heap
			index = index // 2;

		else:
			break;

# Defining heap sort
def heapSort():
	global x;
	while (x >= 0):
		k = heap[0];

		# Taking output of
		# the minimum element
		print(k, end = " ");

		# Set first element
		# as a last one
		heap[0] = heap[x];

		# Decrement of the
		# size of the string
		x = x - 1;

		tmp = -1;

		index = 0;

		length = x;

		# Initializing the left
		# and right index
		left1 = 1;

		right1 = left1 + 1;

		while (left1 <= length):

			# Process of heap sort
			# If root element is
			# minimum than its both
			# of the child then break
			if (heap[index] <= heap[left1] and
				heap[index] <= heap[right1]):
				break;

			# Otherwise checking that
			# the child which one is
			# smaller, swap them with
			# parent element
			else:

				# Swapping
				if (heap[left1] < heap[right1]):
					tmp = heap[index];
					heap[index] = heap[left1];
					heap[left1] = tmp;
					index = left1;

				else:
					tmp = heap[index];
					heap[index] = heap[right1];
					heap[right1] = tmp;
					index = right1;

			# Changing the left index
			# and right index
			left1 = 2 * left1;
			right1 = left1 + 1;

# Utility function
def sort(k, n):
	
	# To heapiFy
	for i in range(n):
		heapForm(k[i]);

	# Calling heap sort function
	heapSort();

# Driver Code
if __name__ == '__main__':
	arr = ["banana", "orange", "apple",
		"pineapple", "berries", "lichi"];

	n = len(arr);

	sort(arr, n);

# This code is contributed by PrinciRaj1992
