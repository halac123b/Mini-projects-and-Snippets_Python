import math


frame_width = 1920
frame_height = 1080

sqrt_len = math.ceil(math.sqrt(len(videos)))
tile_height = frame_height // sqrt_len
tile_width = frame_width // sqrt_len