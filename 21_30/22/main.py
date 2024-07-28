import distro

# String, ID của distribution hiện tại (ubuntu, fedora) dạng lowercase và dùng trong internal code của OS
print(distro.id())

# String, tên cũng giống trên (Ubuntu, Fedora) loại tên show cho user thấy
print(distro.name())
