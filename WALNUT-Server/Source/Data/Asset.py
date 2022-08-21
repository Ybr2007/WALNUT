import pickle  # 用于加载二进制的资源文件   

assetDict : dict[str, object] = {}
otherAssetFiles = [

]

def Init():
    global assetDict
    assetDict = pickle.load(open('./Assets/Asset.asset', 'rb'))
    for file in otherAssetFiles:
        assetDict[file] = pickle.load(open('./Assets/' + file, 'rb'))
