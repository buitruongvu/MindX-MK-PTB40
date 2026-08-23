# Bài 1 (Mức độ: Dễ) - Phân loại kết quả học tập
# Yêu cầu thuật toán: Viết chương trình nhận vào điểm trung bình của một học viên (thang điểm 10) và in ra xếp loại học lực tương ứng. Thuật toán cần có bước kiểm tra tính hợp lệ của dữ liệu đầu vào (điểm không được nhỏ hơn 0 hoặc lớn hơn 10).
# • Từ 8.0 trở lên: 'Giỏi'
# • Từ 6.5 đến dưới 8.0: 'Khá'
# • Từ 5.0 đến dưới 6.5: 'Trung bình'
# • Dưới 5.0: 'Yếu'
# • Ngoài khoảng 0-10: 'Điểm không hợp lệ'
while True:
  avr_score = float(input("Enter your average score: "))
  if avr_score > 10 or avr_score < 0:
    print('Điểm không hợp lệ')
  elif avr_score >= 8.0:
    print('Giỏi')
  elif avr_score >= 6.5:
    print('Khá')
  elif avr_score >= 5.0:
    print('Trung bình')
  else:
    print('Yếu')