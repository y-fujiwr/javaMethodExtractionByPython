# javaMethodExtractionByPython

JavaのメソッドをPythonを使って抽出するスクリプト  
私が研究で使っているスクリプトの，置き場

javalangつこてます．<https://github.com/c2nes/javalang>

#### text_generator.py

seqGAN <https://github.com/LantaoYu/SeqGAN> 用のデータセットを作成するためのスクリプト  
ソースコードのトークンID列(output.txt)と，key:トークン・value:トークンIDのdict(dictionary.pkl)を出力する  
python3 text_generator.py -d ${targetDirectory}  
