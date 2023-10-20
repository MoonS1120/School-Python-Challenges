char = input("Char: ")

def check(char):
  return len(char) == 1 and char.isalpha()
  
print(check(char))
