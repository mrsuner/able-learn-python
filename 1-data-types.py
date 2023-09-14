def main():
    # 整数类型
    int_type = 10
    print(f"整数类型: {int_type}，类型为: {type(int_type)}")

    # 浮点数类型
    float_type = 10.5
    print(f"浮点数类型: {float_type}，类型为: {type(float_type)}")

    # 字符串类型
    string_type = "Hello, Python!"
    print(f"字符串类型: {string_type}，类型为: {type(string_type)}")

    # 列表类型
    list_type = [1, 2, 3, 4, 5]
    print(f"列表类型: {list_type}，类型为: {type(list_type)}")

    # 元组类型
    tuple_type = (1, 2, 3, 4, 5)
    print(f"元组类型: {tuple_type}，类型为: {type(tuple_type)}")

    # 字典类型
    dict_type = {"name": "Alice", "age": 30}
    print(f"字典类型: {dict_type}，类型为: {type(dict_type)}")

    # 集合类型
    set_type = {1, 2, 3, 4, 5}
    print(f"集合类型: {set_type}，类型为: {type(set_type)}")

    # 数据类型转换
    print("\n数据类型转换:")
    int_to_float = float(int_type)
    print(f"整数 {int_type} 转为浮点数: {int_to_float}")

    float_to_int = int(float_type)
    print(f"浮点数 {float_type} 转为整数: {float_to_int}")

    int_to_string = str(int_type)
    print(f"整数 {int_type} 转为字符串: {int_to_string}")

    string_to_list = list(string_type)
    print(f"字符串 '{string_type}' 转为列表: {string_to_list}")

    list_to_tuple = tuple(list_type)
    print(f"列表 {list_type} 转为元组: {list_to_tuple}")

    tuple_to_list = list(tuple_type)
    print(f"元组 {tuple_type} 转为列表: {tuple_to_list}")

if __name__ == "__main__":
    main()
