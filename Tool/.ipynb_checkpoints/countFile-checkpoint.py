import os
import sys


def count_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"错误：'{folder_path}' 不是一个有效的文件夹路径")
        return

    file_count = 0

    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)

    return file_count


def main():
    if len(sys.argv) < 2:
        print("错误：请提供文件夹路径作为命令行参数")
        return

    folder_path = sys.argv[1]
    file_count = count_files_in_folder(folder_path)
    
    print(f"文件夹 '{folder_path}' 中的文件数目为：{file_count}")


if __name__ == "__main__":
    main()
