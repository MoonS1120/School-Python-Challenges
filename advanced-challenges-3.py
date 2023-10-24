medalists = ["Usain Bolt", "Michael Phelps", "Simone Biles", "Nadia Comăneci", "Carl Lewis"]

length = len(medalists) - 1

while length > 0:
  for i in range(length):
    if medalists[i] > medalists[i+1]:
      Temp = medalists[i+1]
      medalists[i+1] = medalists[i]
      medalists[i] = Temp
  length -= 1

# Sorted list: ['Carl Lewis', 'Michael Phelps', 'Nadia Comăneci', 'Simone Biles', 'Usain Bolt']

for i in range(len(medalists)):
  if medalists[i] == "Simone Biles":
    print(f"Index: {i}")
