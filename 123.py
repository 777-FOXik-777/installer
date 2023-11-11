import os

filename = "test.py"

if os.path.exists(filename):
    print(f"{filename} существует в текущем каталоге.")
else:
    print(f"{filename} не существует в текущем каталоге.")
