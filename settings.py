import os
from dotenv import load_dotenv


load_dotenv()


class Resolution:
    h = int(os.getenv("RESOLUTION_H", 640))
    w = int(os.getenv("RESOLUTION_W", 480))
