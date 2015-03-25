# Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20*20 grid?

rows = 20
cols = 20
matrix = [[1] * (rows+1)] * (cols+1)

for i in range(rows - 1, -1, -1):
	for j in range(cols- 1, -1, -1):
		matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]

print(matrix[0][0])