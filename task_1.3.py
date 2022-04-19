def test_number65(x, y):
   if x == 65 or y == 65 or (x+y) == 65:
       return True
   else:
       return False
        
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = test_number65(x, y)
print(result)