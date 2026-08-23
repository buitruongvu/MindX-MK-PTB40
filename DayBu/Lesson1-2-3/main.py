hello = "Hello World!"
print(hello)
# Mọi thứ trong python đều được tổ chức dưới dạng object (object là một đối tượng của một lớp - class )
print(type(hello)) # output: <class 'str'>
a = 1
b = 2
sum = a + b #output: 3
print(sum)
print(type(sum)) #output: <class 'int'>
print(type(type(sum))) #output: <class 'type'>

division = b / a 
print(division) #output: 2.0
print(type(division)) #output: <class 'float'>

is_student = True
print(type(is_student)) #output: <class 'bool'>

#Datatypes
    # int
    # float
    # str
    # bool

# input - output (Nhập - Xuất)
name = input("Enter your name: ") # dòng này sẽ in ra "Enter your name: " và cho phép nhập vào và gán vào biến name. Trả về kiểu dữ liệu: <class 'str'>
print("My name is", name)

# Ép kiểu
my_name = "Đào Xuân Nhật Nam"
str_number = "12"
int_number = int(str_number)
print(int_number) # output: 12
print(type(int_number)) # output: <class 'int'>
# Cách ép kiểu input thành int
age = int(input("Enter your age: "))
print(type(age))

# Cách ép kiểu input thành float
math_score = float(input("Enter your math score: "))
print(type(math_score)) # output: <class 'float'>

# Quy tắc đặt tên biến (Variable Rules)
# Rule 1: Biến chỉ bao gồm chữ in thường (a -> z), chữ in hoa (A->Z), số (0->9) và dấu underscore (_)
      # Hãy xác định tên biến nào là hợp lệ trong các tên biến sau: a68, _123, *abc, ab*, BC6, &12, c#, ...
        # Đáp án: a68, _123, BC6

# Rule 2: Biến không được bắt đầu bằng chữ số.
      # Hãy xác định tên biến nào là hợp lệ trong các tên biến sau: 67z, z68, _3b, A3s, ...
      # Answer: z68, _3b, A3s

# Rule 3: Tên biến phân biệt chữ in hoa và chữ in thường. 
      # Example: A23 and a23 are different     
                
# Rule 4: Tên biến không được trùng với từ khoá
      # Các từ khoá: if, else, True, False, for, in, await, class, def, and,...

# Lesson03: Tính toán toán tử
# Toán tử số học
    # Cộng: +
    # Trừ: -
    # Nhân: *
    # Chia: /
    # Chia lấy phần nguyên: //
    # Chia lấy phần dư: %
    # Mũ: **
# Cộng: +
print(12 + 23) # Cộng số int và int -> output: 35
print(1 + 2.5) # cộng số int và float -> output: 3.5
print("Hello " + "World!") # Cộng chuỗi -> output: "Hello World!"

# Trừ: -
print(23 - 12) # output: 11
print(23.12 - 1.12) # output: 22.0

# Nhân: *
print(12 * 2) # output: 24
print(2.0 * 2) # output: 4.0

# Chia: /
print(12 / 3) # output: 4.0

# Chia lấy phần nguyên: //
print(12 // 3) # output: 4
print(12 // 7) # output: 1

# Chia lấy phần dư: %
print(12 % 3) # output: 0
print(12 % 5) # output: 2

# Mũ: **
print( 2 ** 3) # output: 8
print( 2 ** 2 ** 3) # output: phải thực hiện từ phải qua trái <=> 2 ** (2 ** 3) <=> 2 ** 8 = 256
# Ưu tiên: ** -> *, /, //, % -> +, -

# Toán tử quan hệ: Trả về True hoặc False
# So sánh bằng (==) 
print(2 == 2) # output: True
print(12 == 13) # output: False

# So sánh khác (!=)
print(13 != 13) # output: False
print(13 != 55.2) # output: True

# So sánh lớn hơn (>) và lớn hơn hoặc bằng(>=)
print(12 > 22) # output: False
print( 12 >= 12) # output: True

# So sánh bé hơn (<) và bé hơn hoặc bằng (<=)
print(12 < 22) # output: True
print(22 <= 21) # output: False

# Toán tử Logic
# Phép toán and (và)
print(True and True) #Output: True
print(True and False) #output: False
print(False and False) #output: False

#Phép toán or (hoặc)
print(True or True) #Output: True
print(True or False) #output: True
print(False or False) #output: False

# Phép toán not (Phủ định)
print(not True) #output: False
print(not False) #output: True

# Biểu thức logic
#-----------------------------------------------