from intersect import do_intersect

Parallel = [[0, 0], [1, 1], [0, 1], [1, 2]]
Colinear = [[0, 0], [1, 1], [2, 2], [3, 3]]
ColinearOverlap = [[0, 0], [1, 1], [0, 0], [3, 3]]
ColinearOverlap2 = [[0, 0], [1, 1], [1, 1], [3, 3]]
Intersect = [[0, 0], [2, 2], [2, 0], [0, 2]]
Intersect2 = [[0, 0], [2, 2], [2, 2], [3, 2]]
Self = [[0, 0], [1, 1], [0, 0], [1, 1]]

def main():
	assert(do_intersect(*Parallel) == False)
	assert(do_intersect(*Colinear) == False)
	assert(do_intersect(*ColinearOverlap) == True)
	assert(do_intersect(*ColinearOverlap2) == True)
	assert(do_intersect(*Intersect) == True)
	assert(do_intersect(*Intersect2) == True)
	assert(do_intersect(*Self) == True)
	print "Success"

if __name__ == '__main__':
	main()
