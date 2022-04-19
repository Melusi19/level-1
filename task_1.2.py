def test_number3(x, y):
   if x == 3 or y == 3 or (x+y) == 3:
       return True
   else:
       return False
        
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = test_number3(x, y)
print(result)