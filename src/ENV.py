from dotenv import load_dotenv, find_dotenv
import os

def load():
    load_dotenv(find_dotenv())
def checkEnv():
    load()
    print(
        os.getenv("AWS_DB_ADMIN"),
        os.getenv("AWS_DB_PASSWORD"))
if __name__ == "__main__":
    checkEnv()
else:
    load()