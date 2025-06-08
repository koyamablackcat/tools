import os

# Thư mục chứa file
folder = r"C:\Users\koyama\Documents\AutoFishing\train_img\o2bj"  # ← Thay bằng thư mục thật
start_index = 100000

# Lọc ra file ảnh và file txt
image_exts = ('.jpg', '.jpeg', '.png', '.bmp')
images = [f for f in os.listdir(folder) if f.lower().endswith(image_exts)]
txts = [f for f in os.listdir(folder) if f.lower().endswith('.txt')]

# Tạo set tên file không extension để đối chiếu
image_basenames = {os.path.splitext(f)[0]: f for f in images}
txt_basenames = {os.path.splitext(f)[0]: f for f in txts}

common_basenames = sorted(set(image_basenames.keys()) & set(txt_basenames.keys()))

# Đổi tên các file
for i, basename in enumerate(common_basenames):
    new_name = f"img_{start_index + i}"
    img_old = os.path.join(folder, image_basenames[basename])
    txt_old = os.path.join(folder, txt_basenames[basename])

    img_ext = os.path.splitext(image_basenames[basename])[1]
    img_new = os.path.join(folder, f"{new_name}{img_ext}")
    txt_new = os.path.join(folder, f"{new_name}.txt")

    os.rename(img_old, img_new)
    os.rename(txt_old, txt_new)

    print(f"Đã đổi: {basename} -> {new_name}")

