n = input("Choose position: ")
while True:
   try:
       n = int(n)
       break
   except ValueError:
       n = input("Choose position: ")

if n <= 1:
    element = None
    print("No elements found")
else:
    element = int((2 * n)/ 3) - 1
    print(f"Element located in position n = {n} is {element}")






