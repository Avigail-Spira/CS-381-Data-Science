two = ['a', 'b', 'c']
three = ['d', 'e', 'f']
four = ['g', 'h', 'i']
five = ['j', 'k', 'l']
six = ['m', 'n', 'o']
seven = ['p', 'q', 'r', 's']
eight = ['t', 'u', 'v']
nine = ['w', 'x', 'y', 'z']

def printDigit(d):
  if d == 2:
    return two
  elif d == 3:
    return three
  elif d == 4:
    return four
  elif d == 5:
    return five
  elif d == 6:
    return six
  elif d == 7:
    return seven
  elif d == 8:
    return eight
  elif d == 9:
    return nine

def twoDigits(d):
  a = str(d)[0]
  b = str(d)[1]
  first = printDigit(int(a))
  second = printDigit(int(b))
  for i in range(len(first)):
    for k in range(len(second)):
      print(first[i]+second[k])

def threeDigits(d):
  a = str(d)[0]
  b = str(d)[1]
  c = str(d)[2]
  first = printDigit(int(a))
  second = printDigit(int(b))
  third = printDigit(int(c))
  for i in range(len(first)):
    for k in range(len(second)):
      for j in range(len(third)):
        print(first[i]+second[k]+third[j])

def fourDigits(d):
  a = str(d)[0]
  b = str(d)[1]
  c = str(d)[2]
  d = str(d)[3]
  first = printDigit(int(a))
  second = printDigit(int(b))
  third = printDigit(int(c))
  fourth = printDigit(int(d))
  for i in range(len(first)):
    for k in range(len(second)):
      for j in range(len(third)):
        for l in range(len(fourth)):
          print(first[i]+second[k]+third[j]+fourth[l])
  


def main():
  digit = int(input("Enter a string of maximum 4 digits between 2 and 9: "))

  list = []
  if len(str(digit)) > 4:
    print("That is over the maximum number of digits")

  if len(str(digit)) == 0:
    print("[]")
  elif len(str(digit)) == 1:
    print(printDigit(digit))
  elif len(str(digit)) == 2:
    twoDigits(digit)
  elif len(str(digit)) == 3:
    threeDigits(digit)
  elif len(str(digit)) == 4:
    fourDigits(digit)

if __name__ == '__main__':
  main()
