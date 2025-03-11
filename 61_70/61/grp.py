# Package giúp lấy thông tin về group user trên Linux
import grp

groups = [
    g.gr_gid
    for g in grp.getgrall() # Get data tất cả group (tuple)
    if "username" in g.gr_mem or g.gr_gid == 0  # Từ tuple group, lấy tên/ID group
]