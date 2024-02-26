# Với package này có thể dùng k quan tấm đến OS
# Trên Windows, Path return pathlib.WindowsPath
# Trên Unix, Path return pathlib.PosixPath

from pathlib import Path

# Handle các path quan trọng ở các OS khác nhau
print(Path.home())
