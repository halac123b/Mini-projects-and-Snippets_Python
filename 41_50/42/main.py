import importlib
import sys

# Reload lại 1 package đã import trc đó
## Dùng in case package đã bị thay đổi và cần reload
importlib.reload(sys)
