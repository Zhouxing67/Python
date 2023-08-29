import os


def check_git_repo(folder_path):
    # 检查给定路径是否为 Git 仓库
    if os.path.exists(os.path.join(folder_path, '.git')):
        print(f'{folder_path} 是一个 Git 仓库')
    

    # 遍历子文件夹
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            check_git_repo(dir_path)

# 当前文件夹作为起始路径

current_folder = os.getcwd()
check_git_repo(current_folder)
