# Có 2 loại vòng lặp: 
    # Vòng lặp biết số lần lặp: for
    # Vòng lặp không biết số lần lặp: while

# Practice: Yêu cầu nhập vào số nguyên dương n (Kiểm tra đúng số nguyên dương, nếu nhập số âm hoặc số 0 yêu cầu nhập lại, nhập -1 để thoát) sau đó in ra tổng các chữ số của n.
# Kiểm tra để nhập lại: dùng while
# 123 => "123" => for number in str(n): => int(number) => sum

n = int(input("Enter a positive integer number: "))
while True:
  if n == -1:
    break
  elif n <= 0:
    n = int(input("Please, enter a positive integer number: "))
    continue
  # tong = 0
  # for str_num in str(n):
  #   tong += int(str_num)
  # print(f"Tổng các chữ số của {n} là {tong}")
  tong = sum(int(c) for c in str(n))
  print(f"Tổng các chữ số của {n} là {tong}")
  break
  
    

