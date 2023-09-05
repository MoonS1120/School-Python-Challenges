string = input("String: ")
vowels = ['A','a','E','e','I','i','O','o','U','u']

def make_it_laugh(prompt):
  for letter in prompt:
    if letter in vowels:
      print('haha', end='')
    else:
      print(letter, end='')

make_it_laugh(string)
