
class AdditionGame(object):
	
	def __init__(self, A=None, B=None, C=None, N=None):
		self.A = A
		self.B = B
		self.C = C
		self.N = N
		self.total = 0

	def getMaximiumPoints(self, A, B, C, N):
		self.total = 0
		num_List = [A, B, C]
		max_Val = 0
		while (N > 0):
			max_Val = max(num_List)
			if (max_Val > 0):
				self.total += num_List[num_List.index(max_Val)]
				num_List[num_List.index(max_Val)] -= 1
				# print num_List[0], num_List[1], num_List[2], N, self.total

			N -= 1

		return self.total


aa = AdditionGame()
print aa.GetMaximiumPoints(1,1,1,8)
print aa.GetMaximiumPoints(3,4,5,3)
print aa.GetMaximiumPoints(3,5,48,40)
print aa.GetMaximiumPoints(36,36,36,13)
print aa.GetMaximiumPoints(8,2,6,13)