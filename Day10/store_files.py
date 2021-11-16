import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(BASE_DIR, "images")

# exist_okがTrueだとディレクトリが既存でもエラーを吐かなくなる
os.makedirs(files_dir, exist_ok=True)

# 0 ~ 11までの数字のrangeを返す
my_images = range(0, 12)

for i in my_images:
  fname = f"{i}.txt"
  file_path = os.path.join(files_dir, fname)
  if os.path.exists(file_path):
    print(f'skipped {fname}')
    continue
  with open(file_path, 'w') as f:
    f.write("Hello world")