import os


def delete_empty_folders(folder_path):
    if not os.path.isdir(folder_path):
        print(f"错误：'{folder_path}' 不是一个有效的文件夹路径")
        return

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # 如果文件夹为空
                os.rmdir(dir_path)
                print(f"已删除空文件夹：{dir_path}")


def main():
    folder_path = "C:\Codefield\Python\null"  # 替换为实际的文件夹路径
    delete_empty_folders(folder_path)
 

if __name__ == "__main__":
    main()
