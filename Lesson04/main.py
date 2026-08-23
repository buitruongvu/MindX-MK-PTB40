# Cú pháp câu điều kiện
# if <Điều kiện>: 
    # <Khối lệnh>

#Example: Kiểm tra số dương, nếu là số dương thì in ra là số dương
number = float(input("Enter your number: "))
if number > 0:
  print(f"{number} is a positive number")
elif number == 0:
  print(f"{number} is zero")

# Thực hành 1: Nhập vào một số n từ bàn phím, kiểm tra nếu n là số chẵn thì in ra màn hình câu n là số chẵn , ngược lại in ra màn hình n là số lẻ

# Cú pháp câu điều kiện
# if <Điều kiện>: 
    # <Khối lệnh 1>
# else:
    # <Khối lệnh 2>
n = float(input("Enter your number: "))
if n % 2 == 0:
  print(f"{n} là số chẵn")
else:
  print(f"{n} là số lẻ")

# Cú pháp câu điều kiện đầy đủ
# if <Điều kiện 1>: 
    # <Khối lệnh 1>
# elif <Điều kiện 2>:
    # <Khối lệnh 2>
# elif <Điều kiện 3>:
    # <Khối lệnh 3>
# elif <Điều kiện 4>:
    # <Khối lệnh 4>
# ......
# else:
    # <Khối lệnh n>

