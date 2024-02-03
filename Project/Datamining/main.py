import apriori
import dataPrePocess
import os
import randomData
import time
import psutil


def show_info():
    # 计算消耗内存
    pid = os.getpid()
    # 模块名比较容易理解：获得当前进程的pid
    p = psutil.Process(pid)
    # 根据pid找到进程，进而找到占用的内存值
    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    return memory
    # print(f'{start} 一共占用{memory:.2f}MB')


def main():
    randomData.randomDataGen(valid=False)
    filename = 'shopping_basket_dataset.csv'
    folder_path = './'
    file_path = os.path.join(folder_path, filename)
    dataSet = dataPrePocess.dataGen(file_path)

    restraint = [[0.5, 0.5], [0.55, 0.55], [0.65, 0.7]]
    for minConf, minSupport in restraint:
        print(f'minConf:{minConf :<10} minSupport:{minSupport}\n')

        start_memory = show_info()
        start_time = time.time()
        L, supportData = apriori.apriori(dataSet, minSupport=minSupport)
        print(f'SupportData : {supportData}')
        rules = apriori.generateRules(L, supportData, minConf=minConf)
        for item in rules:
            print(f"{list(item[0])} ---> {list(item[1]) }  conf: {item[2]}")
        end_time = time.time()
        execution_time = end_time - start_time
        end_memory = show_info()
        execution_memory = end_memory - start_memory
        print('S')
        print(f'程序执行时间 {execution_time}')
        print(f'程序占用空间 {execution_memory}MB')
        print('\n')


if __name__ == "__main__":
    main()
