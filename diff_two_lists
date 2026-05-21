# list_diff.py
# -*- coding: utf-8 -*-


def diff_two_lists(list1, list2):
    """
    对比两个列表，返回两个列表：

    only_in_list1：第一个列表中有，但第二个列表中没有的
    only_in_list2：第二个列表中有，但第一个列表中没有的

    特点：
    1. 保留原列表顺序
    2. 不去重
    3. 按值判断是否存在
    """

    set1 = set(list1)
    set2 = set(list2)

    only_in_list1 = []
    only_in_list2 = []

    for item in list1:
        if item not in set2:
            only_in_list1.append(item)

    for item in list2:
        if item not in set1:
            only_in_list2.append(item)

    return only_in_list1, only_in_list2


def main():
    list1 = ["A-1", "A-2", "A-3", "A-4"]
    list2 = ["A-2", "A-4", "A-5", "A-6"]

    only_1, only_2 = diff_two_lists(list1, list2)

    print("第一个列表中有，第二个列表中没有的：")
    print(only_1)

    print("第二个列表中有，第一个列表中没有的：")
    print(only_2)


if __name__ == "__main__":
    main()
