denary_value = input("Denary: ")

print("BCD: ", end='')
for digit in denary_value:
  print(bin(int(digit)).replace('0b','').rjust(4,'0'), end='')
