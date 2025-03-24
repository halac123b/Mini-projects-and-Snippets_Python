import matplotlib.pyplot as plt
import matplotlib
import cv2

# Tạo 1 window Figure chứa cavas dùng để vẽ plot lên đó
## K cần phài luôn gọi lệnh này, vì package tự tạo Figure khi ta call vẽ đồ thị
plt.figure()
# Show ảnh trên canvas, input là image dứoi dạng Numpy array
plt.imshow(train_images[0])

# Switch sang backend Agg, mode chỉ để lưu data vào file chứ k show plot ra UI
matplotlib.use('Agg')