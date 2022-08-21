import pickle  # 用于保存二进制的资源文件
import os  # 用于获取文件路径

from PIL import Image  # 读取图片

assetRootDir = './Assets'  # 资源根目录
assetDict = {}

def LoadFuncManager(fileType: str):
    '''
    通过文件后缀名获取对应的加载函数
    '''
    funcDict: dict[str, callable] = {
        'png': lambda filePath: Image.open(filePath).convert('RGBA'),
        'qss': lambda filePath: open(filePath, 'r').read(),
    }
    if fileType in funcDict:
        return funcDict[fileType]

    raise Exception('没有定义' + fileType + '文件的加载函数')


for root, dirs, files in os.walk(assetRootDir):  # 遍历资源路径
    for file in files:
        if not file.endswith('.asset'):
            # 通过文件后缀名获取对应的加载函数并调用
            data = LoadFuncManager(file.split(
                '.')[-1])(os.path.join(root, file))

            # 将资源保存到字典中
            assetDict[file] = data
            print(file)

with open(assetRootDir + '/Asset.asset', 'wb') as f:
    pickle.dump(assetDict, f)