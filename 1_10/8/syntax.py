import PIL
import numpy as np

# Option xem có cho phép load các ảnh bị truncate hay k
## Ảnh truncate là ảnh có các giá trị pixel bị null
PIL.ImageFile.LOAD_TRUNCATED_IMAGES = True

image_path = "path_to_image"
# Open và read file ảnh
img = PIL.Image.open(image_path)

# Nhưng PIL khác các lib khác, ảnh sẽ k ở sẵn dạng Numpy array
# Convert the image to a NumPy array
img_array = np.array(img)

# Lúc cần convert về lại Image
img = PIL.Image.fromarray(img_array)
# Lưu image
img.save("path_to_save")
