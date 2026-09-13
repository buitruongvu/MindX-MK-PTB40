# Vòng lặp
# 2 loại vòng lặp
    # for (có số lần lặp biết trước)
    # while (không có số lần lặp biết trước)
for i in range(5):
  print(i)

print("="*30)
j = 0 
while j < 5:
  print(j)
  j = j + 1
  
# In các số lẽ từ a đến b, với a và b là 2 số nguyên dương nhập từ bàn phím,    a < b   
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for i in range(a, b+1):
  if i % 2 == 1:
    print(i, end =" ")