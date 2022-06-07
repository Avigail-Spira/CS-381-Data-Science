maxLength = 0
numWithMax = 0

for i in range(1, 1000001):
  list = [i]
  curr = i
  while curr != 1:
    if (curr % 2 == 0):
      curr = curr//2
      list.append(curr)
    elif (curr % 2 != 0):
      curr = 3*curr+1
      list.append(curr)

  if list[-1] !=1:
    list.append(1)

  if (len(list) > maxLength):
    maxLength = len(list)
    numWithMax = i

print(f"The number with the longest sequence is {numWithMax} with a sequence of length {maxLength}")

