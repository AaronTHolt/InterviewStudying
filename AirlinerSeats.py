
class AirlinerSeats(object):
	
	def mostAisleSeats(self, width, seats):
		plane_row = ['.']*width
		num_aisles = width-seats
		num_aisles_left = width-seats

		current_index = 0
		for ii in range(0, seats):
			
			plane_row[current_index] = 'S'

			if ii == 0 and num_aisles_left > 0:
				current_index += 2
				num_aisles_left -= 1
			elif ii == 0 and num_aisles_left == 0:
				current_index += 1
			elif ii > 0 and num_aisles_left > 0:
				if plane_row[current_index-1] == 'S':
					current_index += 2
					num_aisles_left -= 1
				elif plane_row[current_index-1] == '.':
					current_index += 1
			elif ii > 0 and num_aisles_left == 0:
				current_index += 1

			# print plane_row[0:5], current_index, width

		# Reverse list if needed
		for ii in range(0, int(width/2)):
			if plane_row[ii] == '.' and plane_row[width-ii-1] == 'S':
				break
			elif plane_row[ii] == 'S' and plane_row[width-ii-1] == '.':
				plane_row = list(reversed(plane_row))
				break

		# print plane_row

		if width > 100:
			s1 = ''
			s2 = ''
			for ii in range(0, 50):
				s1 += plane_row[ii]
			for ii in range(0, 50):
				s2 += plane_row[ii+width-50] 

			return (s1, s2)

		elif width > 50:
			s1 = ''
			s2 = ''
			for ii in range(0, 50):
				s1 += plane_row[ii]
			for ii in range(0, width-50):
				s2 += plane_row[ii+50]

			return (s1, s2)

		elif width > 0:
			s1 = ''
			for ii in range(0, width):
				s1 += plane_row[ii]

			s1 = str(''.join(s1))
			return s1

aa = AirlinerSeats()
# print aa.mostAisleSeats(6,3)
# print aa.mostAisleSeats(6,4)
# print aa.mostAisleSeats(3,2)
print(aa.mostAisleSeats(12,10))
# print aa.mostAisleSeats(11,7)
# print aa.mostAisleSeats(52,52)
# print aa.mostAisleSeats(200,2)
# print aa.mostAisleSeats(6,3)