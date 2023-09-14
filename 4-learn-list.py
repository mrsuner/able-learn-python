def main():
    # 创建一个列表
    fruits = ["apple", "banana", "cherry"]
    print(f"原始列表: {fruits}")

    # 添加元素到列表的末尾
    fruits.append("orange")
    print(f"\n使用append()添加元素后: {fruits}")

    # 在指定位置插入元素
    fruits.insert(1, "mango")
    print(f"使用insert()插入元素后: {fruits}")

    # 从列表中删除指定元素
    fruits.remove("banana")
    print(f"使用remove()删除元素后: {fruits}")

    # 弹出列表中的最后一个元素
    popped_fruit = fruits.pop()
    print(f"使用pop()后: {fruits}")
    print(f"被弹出的元素是: {popped_fruit}")

    # 获取元素的索引
    index_of_mango = fruits.index("mango")
    print(f"\n'mango'的索引是: {index_of_mango}")

    # 对列表进行排序
    fruits.sort()
    print(f"排序后的列表: {fruits}")

    # 反转列表
    fruits.reverse()
    print(f"反转后的列表: {fruits}")

    # 清空列表
    fruits.clear()
    print(f"\n使用clear()后的列表: {fruits}")


if __name__ == "__main__":
    main()
