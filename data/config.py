from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

import os

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = str(os.environ.get("ADMINS"))
IP = str(os.environ.get("ip"))
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))

# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
