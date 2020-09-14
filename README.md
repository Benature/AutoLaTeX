# AutoLaTeX

[![PyPI](https://img.shields.io/pypi/v/autolatex)](https://pypi.org/project/autolatex/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/autolatex)
[![GitHub stars](https://img.shields.io/github/stars/Benature/AutoLaTeX)](https://github.com/Benature/AutoLaTeX)

Generate LaTeX code by Python for experiment report.

用Python生成LaTeX代码写实验报告。  

>如果有帮助就点个 star 🌟呗  
>欢迎 Pull Request, Fork, 提 issue.

## Features 特性

- 读取excel等表格文件转为latex表格
- ~~(假的)~~ word讲义转tex报告
- 线性拟合等数学处理

## Install 安装

1. `pip`安装：

```shell
pip install -U autolatex
```

2. 源码安装

```shell
git clone git@github.com:Benature/AutoLaTeX.git
cd AutoLaTeX
python setup.py sdist bdist_wheel
pip install -U dist/autolatex-0.x.x-py3-none-any.whl # 其中 0.x.x 处是 pypi 版本号
```

## Usage 使用

1. `xlsx`文件 excel 表格数据转 tex 代码  
   在命令行输入（两种写法等效）：
   ```shell
   autolatex <文件路径>
   alt <文件路径>
   ```
   更多参数说明请用`alt -h`查询。

2. `.py`文件内  
   ```python
   # import autolatex as alt
   from autolatex import table
   df = table.read_excel('data.xlsx')
   print(table.convert(df))
   ```

3. word2tex  
   详见`word2tex`下的 README

