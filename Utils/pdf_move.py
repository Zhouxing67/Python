import os
import shutil


def move_pdfs_to_subfolder(folder_path):
    pdf_folder = os.path.join(folder_path, "PDF")
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            src_path = os.path.join(folder_path, filename)
            dst_path = os.path.join(pdf_folder, filename)
            shutil.move(src_path, dst_path)
            print(f"Moved {filename} to PDF folder.")


# 指定文件夹路径
folder_path = "D:\edge_download"

# 移动PDF文件
move_pdfs_to_subfolder(folder_path)
