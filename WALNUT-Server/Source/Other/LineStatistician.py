'''
统计项目中代码行数
'''
import os

fileType = [
    '.py'
]

root = r'.'
file_lineNum_tuples = []
sum = 0

for dirPath, dirNames, fileNames in os.walk(root):
    for fileName in fileNames:
        if fileName.endswith(tuple(fileType)):
            lineNum = len(open(dirPath + '/' + fileName, 'r', encoding='utf-8').readlines())
            sum += lineNum
            file_lineNum_tuples.append((dirPath + '/' + fileName, lineNum))

file_lineNum_tuples.sort(key=lambda x: x[1], reverse=True)
for file_lineNum in file_lineNum_tuples:
    print(file_lineNum[0], ':', file_lineNum[1])
print('总行数:',sum)