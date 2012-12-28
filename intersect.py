import numpy as np

def do_intersect(p1, p2, q1, q2):
	# s1 = p1 + tr, r = p2 - p1
	# s2 = q1 + us, s = q2 - q1
	r = np.subtract(p2, p1)
	s = np.subtract(q2, q1)
	rxs = np.cross(r, s)
	# if r x s = 0, s1 and s2 are parallel or colinear.
	if rxs == 0:
		# if parallel, (p - q) x r != 0
		if np.cross(np.subtract(p1, q1), r) != 0:
			return False
		else:
			return (q1[0] >= p1[0] and q1[0] <= p1[0] or
					q2[0] >= p1[0] and q2[0] <= p1[0] or
					p1[0] >= q1[0] and p1[0] <= q1[0] or
					p2[0] >= q1[0] and p2[0] <= q1[0]);
		return 
	# s1 and s2 intersect where s1 = s2 where 0 <= t <= 1 and 0 <= u <= 1
	#   (p + tr) x s = (q + us) x s
	# p x s + tr x s = q x s + us x s
	#         tr x s = q x s - p x s
	#              t = (q - p) x s / r x s
	t = np.cross(np.subtract(q1, p1), s) / rxs
	u = np.cross(np.subtract(q1, p1), r) / rxs
	if 0 <= t and 1 >= t and 0 <= u and 1 >= u:
		return True
	else:
		return False
