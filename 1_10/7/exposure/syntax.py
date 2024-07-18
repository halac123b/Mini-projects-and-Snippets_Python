import skimage.exposure
import cv2

facemask = cv2.imread("facemask.png", as_gray=True)

# Scale lại intensity (cường độ sáng) của 1 ảnh grayscale từ inrange=[100, 150] về out_range=[0, 1]
facemask = skimage.exposure.rescale_intensity(
    facemask, in_range=(100, 150), out_range=(0, 1)
)
