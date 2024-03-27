import dotenv

dotenv.load_dotenv()
# Options:
  # override=True: value trong file .env sẽ override lại biến env nếu nó đã có sẵn (default: False)

import os  # provides ways to access the Operating System and allows us to read the environment variables

my_id = os.getenv("ID")
my_secret_key = os.getenv("SECRET_KEY")
