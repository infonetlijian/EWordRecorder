# Try to write the first Python program of my own
# Python version:3.5
# coding : UTF-8
import os


def EnglishWordRecord(LibraryName, Word):
    try:
        EWordLibrary = open(LibraryName, "r+")  # 读写方式打开文件
        allContents = []  # 列表
        for eachLine in EWordLibrary:
            allContents.append(eachLine)
        print(allContents)
        allContents.append(Word)
        print(allContents)
        str = ''.join(allContents)  # join()将序列用\n相连接
        print(str)
        position = EWordLibrary.tell()  # 当前文件指针位置
        if position != 0:
            position = EWordLibrary.seek(0, 0)  # 重新将指针定位到文件的开头
        EWordLibrary.write(str + "\n")
    finally:
        EWordLibrary.close()
    return


print(os.getcwd())  # 获取当前工作目录
EnglishWordRecord("EWordLibrary.txt", "test2, this is a test2")


def createLibraryFile(fileName):
    # os.mknod(fileName)#macOS下需要超级用户权限
    open(fileName, 'w').close()  # 创建文件
    # with open(fileName, 'w') as file: #创建后立即写入数据
    #      file.write('hello world')
    return
