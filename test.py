'''
read input
'''
books = []	 #(val, scanned?)
libraries = [] #([book_id...], signup, books/day)

filename = 'b_read_on.txt'
file = open(filename, 'r')
problemStat = file.readline().split()
bookStat = file.readline()
for value in bookStat.split():
	books.append((int(value),False))


def findValue(id):
	return books[id][0]


for i in range(int(problemStat[1])): # int(problemStat[1]) is total num of libraries
	stat = file.readline().split()
	libStat = ([], int(stat[1]), int(stat[2]))
	libBooks = file.readline().split()
	for book in libBooks:
		libStat[0].append(int(book))
		
	libStat[0].sort(key = findValue)
	libraries.append(libStat)




"""
find library stats
"""
def calc_lib_val(lib, day):
	score = 0
	numBooks = day * lib[2]
	for i in range(numBooks):
		pass
	"""
	for i in range(day):
		for num in range(lib[2]):
			if (i*lib[2]+num < len(lib[0])):
				book_id = lib[0][i*lib[2] + num]
				if (books[book_id][1]):
					score += books[book_id][0] #adds next book to score
	"""
	return score

def calc_effic(lib, days_active, signup_time):
	val = calc_lib_val(lib, days_active + signup_time)
	return val/(days_active + signup_time)
	
"""
determine library signup order
"""


"""
determine book scanning order
"""

"""
output
"""
