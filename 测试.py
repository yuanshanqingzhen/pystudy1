# while(1):
#         try:
#             num = int(input("请输入一个数字: "))
#             result = 10 / num
#         except ValueError:
#             print("错误：请输入有效的数字！")
#         except ZeroDivisionError:
#             print("错误：不能除以零！")
#         else:
#             print(f"结果是: {result}")
#             break


# try:
#     # 可能会出错的代码
#     file = open("不存在的文件.txt", "r")
# except Exception as e:
#     print(f"发生错误：{e}")


# try:
#     num = int(input("请输入一个数字: "))
#     result = 10 / num
# except Exception as e:
#     print(f"发生错误：{e}")


# try:
#     result = 10 / 0
# except Exception as e:
#     print(f"错误类型：{type(e).__name__}")
#     print(f"错误信息：{e}")


try:
    num = int(input("请输入一个数字: "))
    result = 10 / num
except ValueError:
    print("错误：请输入有效的数字！")
    pass
except ZeroDivisionError:
    print("错误：不能除以零！")
    pass
else:
    print(f"结果是: {result}")