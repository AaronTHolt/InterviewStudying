

class BinaryHeap(object):
	def __init__(self):
		self.heapList = []
		self.currentSize = 0

	def insert(self, data):
		'''Insert data into heap'''
		self.heapList.append(data)
		self.currentSize += 1
		self.fixUpHeap(self.currentSize-1)

	def fixUpHeap(self, ii):
		'''Helper funcion that shifts the latest insert
		up to its correct position'''
		#The ii+1 makes sure the root node is checked too
		while (ii+1) / 2 > 0:
			#if heap property not intact
			if self.heapList[ii] < self.heapList[ii/2]:
				self.heapList[ii/2], self.heapList[ii] = self.heapList[ii], self.heapList[ii/2]
			ii /= 2

	def printInorder(self):
		'''Print the heap in order'''
		for ii in self.heapList:
			print ii,
		print ''

	def deleteMin(self):
		'''Delete root node'''

		#First swap with last value
		lastIndex = self.currentSize-1
		self.heapList[0], self.heapList[lastIndex] = self.heapList[lastIndex], self.heapList[0]

		#Delete last node
		self.heapList.pop()
		#update size
		self.currentSize -= 1

		#fix heap
		self.fixDownHeap(0)


	def fixDownHeap(self, pos):
		'''Helper funciton that shifts an entry
		down after a delete min operation'''

		#while there's at least one child
		while (2*pos + 1) < self.currentSize:

			# print self.heapList, self.currentSize, pos, 2*pos+1, 2*pos+2

			#2 children
			if (2*pos + 2) < self.currentSize:
				# print self.heapList[pos], self.heapList[2*pos + 1], self.heapList[2*pos + 2]
				#check left
				if (self.heapList[pos] > self.heapList[2*pos + 1] and
					self.heapList[2*pos + 1] <= self.heapList[2*pos + 2]):
					temp = int(self.heapList[pos])
					self.heapList[pos] = self.heapList[2*pos + 1]
					self.heapList[2*pos + 1] = temp
					pos = 2*pos + 1
				#check right
				elif self.heapList[pos] > self.heapList[2*pos + 2]:
					temp = int(self.heapList[pos])
					self.heapList[pos] = self.heapList[2*pos + 2]
					self.heapList[2*pos + 2] = temp
					pos = 2*pos + 2

				else:
					break

			#1 child
			elif (self.heapList[pos] > self.heapList[2*pos + 1]):
					temp = int(self.heapList[pos])
					self.heapList[pos] = self.heapList[2*pos + 1]
					self.heapList[2*pos + 1] = temp
					pos = 2*pos + 1

			#Otherwise end
			else:
				break

	def heapSort(self):
		'''Destroy the heap and leave a sorted array'''

		while self.currentSize > 0:
			self.printInorder()
			#First swap with last value
			lastIndex = self.currentSize-1
			self.heapList[0], self.heapList[lastIndex] = self.heapList[lastIndex], self.heapList[0]

			#'Delete' last node
			self.currentSize -= 1

			#fix heap
			self.fixDownHeap(0)

	def heapify(self, a_list):
		'''Make a heap out of a a_list
		destroys current heap'''
		self.heapList = a_list
		self.currentSize = len(a_list)

		rows = 0
		temp = int(self.currentSize)+1
		while temp > 0:
			temp /= 2
			rows += 1

		#first parent
		currentParent = 2**rows - 2

		#fix all parents
		while currentParent >= 0:
			self.fixDownHeap(currentParent)
			currentParent -= 1



def testBinHeap():
	'''Basic test cases for the above 
	BinaryHeap class'''

	heap = BinaryHeap()
	for ii in range(2,11,2):
		heap.insert(ii)	

	assert heap.heapList[0] == 2
	assert heap.heapList == [2,4,6,8,10]

	heap.insert(0)
	heap.insert(-2)
	assert heap.heapList[0] == -2

	heap.delete_min()
	assert heap.heapList[0] == 0

	heap.heapSort()
	assert heap.heapList == [10,8,6,4,2,0]

	a_list = [1,5,23,4,77,1234,-2,-7,1,0]
	test_list = list(a_list)
	heap.heapify(a_list)
	heap.heapSort()
	assert heap.heapList == list(reversed(sorted(test_list)))
	



testBinHeap()