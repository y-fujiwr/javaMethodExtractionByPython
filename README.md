# javaMethodExtractionByPython

JavaのメソッドをPythonを使って抽出するスクリプト  
私が研究で使っているスクリプトの，置き場

javalangつこてます．<https://github.com/c2nes/javalang>

### forSeqGAN.py

seqGAN <https://github.com/LantaoYu/SeqGAN> 用のデータセットを作成するためのスクリプト  
ソースコードのトークンID列(output.txt)と，key:トークン・value:トークンIDのdict(dictionary.pkl)を出力する  
python3 forSeqGAN.py -d ${targetDirectory}  

### preprocess_roy.py

Semantic Benchmark <https://drive.google.com/file/d/1KicfslV02p6GDPPBjZHNlmiXk-9IoGWl/view> を ASTNN <https://github.com/zhangj111/astnn> の入力形式に変換するためのスクリプト
Semantic Benchmarkの論文： Farouq, Al-omari, Chanchal K. Roy, and Tonghao Chen, SemanticCloneBench: A Semanti Code Clone Benchmark using Crowd-Source Knowledge, Proc. of IWSC 2020, pp.57-63, London, ON, Canada, Feb. 2020.
