n = int(input("Nhập số nguyên n: "))

if n < 2:
  prime = False
else:
  for i in range(2, n):
    if n % i == 0:
      prime = False
  
  prime = True

if prime:
  print(n, "là số nguyên tố")
else:
  print(n, "không là số nguyên tố")
print("a") if prime else print("b")
  