# Toán tử (Operators)
# 1. Toán tử số học
a = 12 + 34 # toán tử cộng
b = 12 - 15 # toán tử trừ
c = 6 * 8 # toán tử nhân 
d = 8 / 2 # toán tử chia. Lưu ý output là float
e = 13 // 2 # toán tử chia lấy phần nguyên
f = 13 % 2 # toán tử chia lấy phần dư
g =  2 ** 3 # Toán tử mũ

h = 2 ** 2 ** 3 # tương đương với 2 ** (2 ** 3) # Thực hiện từ phải qua trái
# Thứ tự ưu tiên: ** -> *, /, //, % -> +, -

# Ngoài ra còn có các phép toán thao tác với kiểu chuỗi (string)
# Phép cộng (+):
print("Hello " + "World")
# Phép nhân (*):
print("Hi" * 3)
print("hi" * 0)
print("9" * 3) #output: "999"

# 2. Toán tử quan hệ (là phép so sánh trả về kiểu dữ liệu Boolean, True hoặc False)
# So sánh bằng (==):
a = 3
print(a == 3) # output: True
print(5 == 5) # output: True
print(3 == 5) # output: False

# So sánh khác (!=):
x = 12
y = 15
print(x != y) #output: True
print(x != 12) #output: False

# So sánh lớn hơn (>), lớn hơn hoặc bằng (>=)
print(x > y) #output: False
print(x >= 12) #output: True

# So sánh bé hơn (<), bé hơn hoặc bằng (<=)
x = 12
y = 15
print(x < y) #output: True
print(y <= 11) #output: False

# 3. Toán tử logic 
# Bao gồm and, or và not
# Về Truthy và Falsy
# Trong Python, "truthy" và "falsy" (hoặc falsey) là thuật ngữ dùng để chỉ cách các giá trị được đánh giá khi chúng nằm trong một điều kiện logic (ngữ cảnh boolean), ví dụ như trong câu lệnh if hoặc vòng lặp while.
# Gợi mở
print(">>>>", bool(13)) 
print(">>>>", bool(0))
# Các giá trị Falsy (Đánh giá là False) là những giá trị nào ép thành kiểu boolean nhận giá trị False
# Các giá trị Falsy: 
      # None, False (Hằng số được định nghĩa sẵn)
      # 0, 0.0, 0j, (Các loại số bằng Không (Zero))
      # "", '', """""" (Các chuỗi (String) rỗng)
      # [] (list), () (tuple), {} (dict), set(), range(0) Các cấu trúc dữ liệu rỗng

# Các giá trị Truthy (Đánh giá là True) là những giá trị nào ép thành kiểu boolean nhận giá trị True
# Các giá trị Truthy là các giá trị còn lại

print(bool(""))
print(bool("0"))

# and (và)
print(True and True) #output: True
print(True and False) #output: False
print(False and False) #output: False

# or (hoặc)
print(True or True) #output: True
print(True or False) #output: True
print(False or False) #output: False

# not (Phủ định)
print(not True) #output: False
print(not False) #output: True
print(">>", not 3) #output: False
print(">>>", not "0") #output: False

# 4. Biểu thức logic 
x, y, z = 10, 6, 8
a = x < 12 and z > 6 # True
b = x > 15 or y < 8 # True
c = not b # False

# link bài practice: https://docs.google.com/forms/d/e/1FAIpQLSeyrSScLkJT8PnHje0BeGVDlVWRi_5pyEN-kSatTHzs4M5ZfA/viewform
