def LEFT(string,length):   
  return string[:length]

def RIGHT(string,length):
  return string[-1:-length:-1]

def MID(string,start,end):
  return string[start:end]
    
def LENGTH(string):
  return len(string)

def LCASE(character):
  if character.islower():
    return character
    
def UCASE(character):
  if character.isupper():
    return character

def TO_UPPER(string):
  return string.upper()

def TO_LOWER(string):
  return string.lower()
 
def NUM_TO_STRING(num):
  return str(num)

def STRING_TO_NUM(str):
  return int(str)

def ASC(character):
  return ord(character)

print(LEFT("hello",2))
print(TO_UPPER("hello"))
print(ASC("a"))
