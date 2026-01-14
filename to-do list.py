tasks = []
while True:
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")

    choice = input("请选择功能: ")



    if choice == "1":
        if len(tasks) == 0:
            print("暂无任务")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")


    if choice == "2":
        task = input("请输入你的任务")
        tasks.append(task)

    if choice == "3":
        index = int(input("请输入你要删除的任务编号") )
        tasks.pop(index - 1)

    if choice == "4":
        break


