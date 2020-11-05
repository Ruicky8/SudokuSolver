grid = [
	[5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,0,0]
]

def print_board(grid):
	for i in range(9):
		if i % 3 == 0 and i != 0:
			print("---------------------")
		for j in range(9):
			if j % 3 == 0 and j != 0:
				print("|", end = " ")
			print(grid[i][j], end = " ")
		print("")

def find_blank(grid):
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				return i, j
	return False

def valid(grid, i, j, n):
	for row in range(9):
		if n == grid[row][j]:
			return False
	
	for col in range(9):
		if n == grid[i][col]:
			return False
	
	box_i = i / 3
	box_j = j / 3
	for row in range(int(box_i) * 3, int(box_i) * 3 + 3):
		for col in range(int(box_j) * 3, int(box_j) * 3 + 3):
			if row != i and col != j:
				if n == grid[row][col]:
					return False
	return True
	
def solve(grid):
	empty = find_blank(grid)
	if empty == False:
		print("\n=====================\n")
		print_board(grid)
		if(input("More? (Y/N): ") == 'Y'):
			return False
		return True
	else:
		i, j = empty
	for n in range(1,10):
		if valid(grid, i, j, n):
			grid[i][j] = n
			if solve(grid):
				return True
			else:
				grid[i][j] = 0			
	return False	
			

print_board(grid)
solve(grid)
