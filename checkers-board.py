n, m = map(int, input("Board: ").split(','))
board = []

for i in range(n):
  temp = []
  for j in range(m):
    if (i+j)%2 == 0:
        temp.append('.')
    else:
        temp.append('*')
  board.append(temp)

for line in board:
  print(line)
