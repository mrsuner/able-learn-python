def main():
    items = []  # 初始化一个空的list

    while True:
        # 打印菜单
        print("\n操作菜单:")
        print("1. 添加字符串到列表")
        print("2. 从列表中删除字符串")
        print("3. 退出")

        choice = input("请选择操作 (1/2/3): ")

        # 根据用户的选择进行操作
        if choice == "1":
            # 添加字符串到list
            string_to_add = input("请输入要添加的字符串: ")
            items.append(string_to_add)
            print("当前列表内容:", items)

        elif choice == "2":
            # 从list中删除字符串
            string_to_remove = input("请输入要删除的字符串: ")
            if string_to_remove in items:
                items.remove(string_to_remove)
                print("当前列表内容:", items)
            else:
                print("该字符串不在列表中!")

        elif choice == "3":
            # 退出程序
            print("谢谢使用!")
            break

        else:
            print("无效的选择，请重新输入!")


if __name__ == "__main__":
    main()
