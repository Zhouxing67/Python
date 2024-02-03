import random
import csv

# 具体的物品名
items = [
    "milk",
    "beer",
    "pea",
    "bread",
    "cheese",
    "chocolate",
    "coffee",
    'fish',
]


def randomDataGen(items=items, minNum=4, maxNum=7, tranNum=50, valid=False):
    # 生成购物篮数据集
    if valid is False:
        return
    dataset = []
    for _ in range(tranNum):
        # 每个事务至少包含四件不重复的物品
        num_items = random.randint(minNum, maxNum)
        basket = random.sample(items, num_items)
        dataset.append(basket)

    # 写入CSV文件
    with open(
        "shopping_basket_dataset.csv", mode="w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerows(dataset)
