# range(n): Chạy từ 0 -> n - 1: start = 0, end = n, step = 1
# range(a, b): Chạy từ a -> b - 1: start = a, end = b, step = 1
# range(a, b, c): Chạy từ a -> b - 1: start = a, end = b, step = c
print(list(range(6))) # output: [0, 1, 2, 3, 4, 5]
print(list(range(3, 10))) # output: [3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 26, 5))) # output: [5, 10, 15, 20, 25]

# Thiết An: range(5, 21)

for i in range(8):
  print(i, end=" ") # output: 0 1 2 3 4 5 6 7

# Practice: Nhập vào số nguyên dương n, sau đó in ra các số chẵn và tính tổng của các số lẻ từ 0 đến n.
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(n + 1):
  if i % 2 == 0:
    print(i, end=" ")
  else:
    sum += i # sum = sum + i
print(f"sum of add number is {sum}")

    
