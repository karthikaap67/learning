def multiply(x1, x2):
  return x1 * x2

if __name__ == '__main__':
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  mul = multiply(num1, num2)
  print("The product of given numbers is {} ".format(mul))
