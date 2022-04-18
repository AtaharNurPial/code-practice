'''problem statement: return the total number of unique shape can drawn from 
a mxn grid. position can be changed only 1 step by right or down'''

def grid_path(m,n):
	if m == 0 or n == 0:
		return 1
	else:
		return grid_path(m-1,n) + grid_path(m,n-1)
print(f"{grid_path(4,2) = }")
