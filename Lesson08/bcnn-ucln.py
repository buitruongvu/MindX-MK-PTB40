# Bội chung nhỏ nhất của a và b là số nhỏ nhất đều chia hết cho a và chia hết cho b
# BCNN(6, 9) = 18
# Ước chung lớn nhất của a và b là số lớn nhất mà a và b đều chia hết cho số đó
# UCLN(18, 24) = 6

x, y = 12, 4
print("x", x)
print("y", y)
print(24 % 18)

a = int(input("Enter a natural number as a: ")) # a = 18
b = int(input("Enter a natural number as b: ")) # b = 24

b = min(a, b) # b = min(18, 24) = 18
a = max(a, b) # a = max(18, 24) = 24

temp_a, temp_b = a, b # temp_a = 24, temp_b = 18

while temp_b != 0: 
  temp_a, temp_b = temp_b, temp_a % temp_b
  # step1: temp_a = 24, temp_b = 18 => temp_b = 18 != 0 =>  temp_a = 18, temp_b = 6
  # step2: temp_a = 18, temp_b = 6 => temp_b = 6 != 0 => temp_a = 6, temp_b=16%8 =0
  # step3: temp_a = 6, temp_b = 0 => temp_b = 0 == 0 => ucln = temp_a = 6
ucln = temp_a

bcnn = (a * b) // ucln
print(f"BCNN of {a} and {b} is {bcnn}")
print(f"UCLN of {a} and {b} is {ucln}")

