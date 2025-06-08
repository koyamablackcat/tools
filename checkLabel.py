import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import os

class LabelImageChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kiểm tra nhãn và ảnh")

        # Nút chọn ảnh
        self.btn_select = tk.Button(self.root, text="Chọn ảnh", command=self.select_image)
        self.btn_select.pack(pady=10)

        # Canvas để hiển thị ảnh
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

        # Label hiển thị thông tin nhãn
        self.info_label = tk.Label(self.root, text="")
        self.info_label.pack(pady=5)

        self.root.mainloop()

    def select_image(self):
        img_path = filedialog.askopenfilename(
            title="Chọn file ảnh",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if not img_path:
            return

        # Lấy đường dẫn label tương ứng
        label_path = os.path.splitext(img_path)[0] + ".txt"

        # Load ảnh và nhãn
        self.load_image_and_label(img_path, label_path)

    def load_image_and_label(self, img_path, label_path):
        try:
            self.img = Image.open(img_path).convert("RGB")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mở ảnh:\n{e}")
            return

        self.width, self.height = self.img.size

        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                line = f.readline().strip()
                if line:
                    parts = line.split()
                    self.class_id = int(parts[0])
                    self.cx, self.cy, self.nw, self.nh = map(float, parts[1:5])
                else:
                    self.class_id = None
        else:
            self.class_id = None

        self.root.geometry(f"{self.width}x{self.height+80}")  # Resize cửa sổ cho vừa ảnh + info

        self.canvas.config(width=self.width, height=self.height)

        self.draw_image_with_bbox()

        if self.class_id is not None:
            self.info_label.config(text=f"Class ID: {self.class_id}, Center: ({self.cx:.2f}, {self.cy:.2f}), Size: ({self.nw:.2f}, {self.nh:.2f})")
        else:
            self.info_label.config(text="Không có nhãn tương ứng hoặc file nhãn rỗng")

    def draw_image_with_bbox(self):
        img_draw = self.img.copy()
        draw = ImageDraw.Draw(img_draw)

        if self.class_id is not None:
            x1 = (self.cx - self.nw/2) * self.width
            y1 = (self.cy - self.nh/2) * self.height
            x2 = (self.cx + self.nw/2) * self.width
            y2 = (self.cy + self.nh/2) * self.height
            draw.rectangle([x1, y1, x2, y2], outline="red", width=2)

        self.tk_img = ImageTk.PhotoImage(img_draw)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)

if __name__ == "__main__":
    LabelImageChecker()
