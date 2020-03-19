import javalang
import javalang.ast as ast
from collections import defaultdict
import argparse
from pathlib import Path
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('-d','--directory',type=str)
parser.add_argument('-l','--language',type=str,default='java')
parser.add_argument('-o','--outputFileName',type=str,default='output.txt')
args = parser.parse_args()

fileGenerator = Path(args.directory).glob("**/*.{}".format(args.language))
text = "class a {\n"
for f in fileGenerator:
    text = text + open(str(f)).read()
text = text + "}\n"
tokens = list(javalang.tokenizer.tokenize(text))

positions = []

#各メソッドの位置をpositionsに保存
tree = javalang.parse.parse(text)
for _, node in tree.filter(javalang.tree.MethodDeclaration):
    positions.append(node.position)

nest = 0
output_text = ""
output = open(args.outputFileName,"w")

def getDictSize():
    return len(dictionary)

dictionary = defaultdict(getDictSize)
methods = [[]]

for token in tokens:
    i = 0
    if token.position[0] >= positions[i].line:
        if token.value == "{":
            nest += 1
        if nest > 0:
            #書き込み
            methods[-1].append(str(dictionary[token.value]))
        if token.value == "}":
            nest -= 1
            if nest == 0:
                i += 1
                methods.append([])

#短いメソッドを削除
methodStr = []
for m in methods:
    if len(m) >= 20:
        methodStr.append(" ".join(m))

outputText = "\n".join(methodStr) + "\n"

output.write(outputText)
pickle.dump(dict(dictionary),open("dictionary.pkl","wb"))
