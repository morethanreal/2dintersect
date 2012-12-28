from intersect import do_intersect

Parallel = [[0, 0], [1, 1], [0, 1], [1, 2]]
Colinear = [[0, 0], [1, 1], [2, 2], [3, 3]]
ColinearX = [[0, 0], [1, 0], [2, 0], [3, 0]]
ColinearY = [[0, 0], [0, 1], [0, 2], [0, 3]]
ColinearOverlap = [[0, 0], [3, 3], [1, 1], [4, 4]]
ColinearOverlap1 = [[0, 0], [1, 1], [1, 1], [3, 3]]
ColinearOverlapX = [[0, 0], [2, 0], [1, 0], [3, 0]]
ColinearOverlapY = [[0, 0], [0, 2], [0, 1], [0, 3]]
Intersect = [[0, 0], [2, 2], [2, 0], [0, 2]]
Intersect2 = [[0, 0], [2, 2], [2, 2], [3, 2]]
Self = [[0, 0], [1, 1], [0, 0], [1, 1]]

def main():
	assert(do_intersect(*Parallel) == False)
	assert(do_intersect(*Colinear) == False)
	assert(do_intersect(*ColinearX) == False)
	assert(do_intersect(*ColinearY) == False)
	assert(do_intersect(*ColinearOverlap) == True)
	assert(do_intersect(*ColinearOverlap1) == True)
	assert(do_intersect(*ColinearOverlapX) == True)
	assert(do_intersect(*ColinearOverlapY) == True)
	assert(do_intersect(*Intersect) == True)
	assert(do_intersect(*Intersect2) == True)
	assert(do_intersect(*Self) == True)
	print "Success"

if __name__ == '__main__':
	main()
