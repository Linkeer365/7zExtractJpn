import os

# 7z.exe必须加入环境变量里，否则会报7z找不到命令！
myDir = input("大文件夹绝对路径：")

os.chdir(myDir)

for filename in os.listdir(myDir):
    if filename.endswith(".zip"):
        # shift-jis 对应932编码，其他的自己搜搜吧
        # -o 后面没有空格，切记切记...
        command = f'7z x "{filename}" -mcp=932 -o"./{filename.replace(".zip","")}/"'
        print(command)
        os.system(command)