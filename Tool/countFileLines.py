import sys


def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except OSError as e:
        print(f"错误：无法打开文件 '{file_path}'")
    except Exception as e:
        print(f"错误：发生了错误 - {str(e)}")


def main():
    if len(sys.argv) < 2:
        print("错误：请提供文件路径作为命令行参数")
        return

    file_path = sys.argv[1]
    line_count = count_lines_in_file(file_path)

    if line_count is not None:
        print(f"文件 '{file_path}' 的行数为：{line_count}")


if __name__ == "__main__":
    main()
