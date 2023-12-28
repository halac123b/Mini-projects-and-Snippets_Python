import dotenv

dotenv.load_dotenv()

import os  # provides ways to access the Operating System and allows us to read the environment variables

my_id = os.getenv("ID")
my_secret_key = os.getenv("SECRET_KEY")
