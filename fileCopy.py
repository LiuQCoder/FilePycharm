import shutil,os

fileList = []
filepath = input("输入路径")
copypath =input("请输入需要复制的文件")
for folderName ,subfolders,filenames in os.walk(filepath):
    if  subfolders == []:
        fileList.append(folderName)
for path in fileList:
    shutil.copy(copypath,path)