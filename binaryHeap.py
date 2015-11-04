

class BinaryHeap(object):
	def __init__(self):
		self.heapList = []
		self.currentSize = 0

	def insert(self, data):
		self.heapList.append(data)
		self.currentSize += 1
		self.fixUpHeap(self.currentSize-1)

	def fixUpHeap(self, ii):
		#The ii+1 makes sure the root node is checked too
		while (ii+1) / 2 > 0:
			#if heap property not intact
			if self.heapList[ii] < self.heapList[ii/2]:
				self.heapList[ii/2], self.heapList[ii] = self.heapList[ii], self.heapList[ii/2]

			ii /= 2

	def printInorder(self):
		for ii in self.heapList:
			print ii


def test_bin_heap():
	heap = BinaryHeap()
	for ii in range(2,11,2):
		heap.insert(ii)	

	assert heap.heapList[0] == 2
	assert heap.heapList == [2,4,6,8,10]

	heap.insert(0)
	heap.insert(-2)

	assert heap.heapList[0] == -2



test_bin_heap()