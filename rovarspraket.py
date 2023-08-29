prompt = input("English: ")

vowels = ['A','a','E','e','I','i','O','o','U''u', ' ']

print("Rövarspråket: ", end='')
for letter in prompt:
  if letter in vowels:
    print(letter, end='')
  else:
    print(f"{letter}o{letter}", end='')
