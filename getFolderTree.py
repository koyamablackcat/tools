import os

def list_dir_tree_to_md(folder_path, output_md_path):
    lines = []

    def recurse(path, indent=0):
        for item in sorted(os.listdir(path)):
            full_path = os.path.join(path, item)
            prefix = "    " * indent + "- " + item
            lines.append(prefix)
            if os.path.isdir(full_path):
                recurse(full_path, indent + 1)

    recurse(folder_path)

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("# Cây thư mục\n\n")
        f.write("\n".join(lines))

# Ví dụ sử dụng:
folder = r"C:\Users\koyama\Documents\AutoFishing"           # ← Thay bằng thư mục cần quét
output_md = "output_folder_structure.md" # ← File markdown đầu ra

list_dir_tree_to_md(folder, output_md)
print(f"Đã lưu cây thư mục vào: {output_md}")
