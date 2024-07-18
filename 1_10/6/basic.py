# Với package này có thể dùng k quan tấm đến OS
import pathlib

# Handle các path quan trọng ở các OS khác nhau
# Trên Windows, Path return pathlib.WindowsPath
# Trên Unix, Path return pathlib.PosixPath
print(pathlib.Path.home())

# Iterate qua từng file và folder trong folder
for f in pathlib.Path.home().iterdir():
    # is_file(): check xem path đó có phải là 1 file k
    print(f"{f.name} is a file: {f.is_file()}")
