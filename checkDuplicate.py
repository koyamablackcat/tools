import os
import hashlib

# Tính hash của file
def get_file_hash(file_path, hash_algo=hashlib.md5):
    hash_obj = hash_algo()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# Duyệt tất cả file trong thư mục và thư mục con
def find_duplicate_files(root_dir):
    hash_map = {}  # hash: list of file paths
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_hash = get_file_hash(file_path)
                hash_map.setdefault(file_hash, []).append(file_path)
            except Exception as e:
                print(f"Lỗi khi xử lý {file_path}: {e}")
    return hash_map

# Xóa các file trùng, giữ lại 1 file duy nhất
def delete_duplicates(duplicates_map):
    total_deleted = 0
    for file_list in duplicates_map.values():
        if len(file_list) > 1:
            # Giữ lại file đầu tiên, xóa phần còn lại
            for file_to_delete in file_list[1:]:
                try:
                    os.remove(file_to_delete)
                    print(f"Đã xóa: {file_to_delete}")
                    total_deleted += 1
                except Exception as e:
                    print(f"Lỗi khi xóa {file_to_delete}: {e}")
    print(f"Đã xóa tổng cộng {total_deleted} file trùng.")

# Đường dẫn thư mục gốc
root_directory = r"C:\Users\koyama\Documents\AutoFishing\train_img"  # ← Thay bằng đường dẫn thật

duplicates = find_duplicate_files(root_directory)
delete_duplicates(duplicates)
