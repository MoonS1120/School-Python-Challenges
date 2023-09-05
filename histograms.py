numbers = input("Number: ").split(',')

def histogram(l):
  for num in l:
    print('*'*int(num))

histogram(numbers)
