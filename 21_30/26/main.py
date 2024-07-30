import gc

# Gọi dọn rác 1 cách thủ công
## Thường chỉ dùng nếu tại đó chương trình có 1 lượng memory thừa cần đc dọn dẹp ngay
## Vì lệnh này đc Python gọi tự động, nên gọi thủ công thường là k cần thiết, vì nặng
gc.collect()
