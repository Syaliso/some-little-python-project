while True:
    print("欢迎来到kim的计算器")
    print("我们允许四种运算符号+ - * /")
    print("按p可以推出计算器")

    user_input = input("请输入你的第一个数字(按p可以退出): ")
    if user_input == "p":
        break

    try:
        num1 = float(user_input)
    except ValueError:
        print("非法的数字")
        continue

    operator = input("请打入你的运算符号(+ - * /) :")

    if operator not in ("+", "-", "*", "/"):
        print("非法的符号")
        continue

    try:
        num2 = float(input("请输入第二个数字"))
    except ValueError:
        print("非法的数字")
        continue

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("没法除0")
            continue
        else:
            result = num1 / num2


    print(result)