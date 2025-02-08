# AutoLaTeX

[![PyPI](https://img.shields.io/pypi/v/autolatex)](https://pypi.org/project/autolatex/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/autolatex)
[![GitHub stars](https://img.shields.io/github/stars/Benature/AutoLaTeX)](https://github.com/Benature/AutoLaTeX)

Generate LaTeX code by Python for experiment report.

用 Python 生成 LaTeX 代码写实验报告。

> 如果有帮助就点个 star 🌟 呗  
> 欢迎 Pull Request, Fork, 提 issue.

## Features 特性

- 读取 excel 等表格文件转为 latex 表格
- ~~(假的)~~ word 讲义转 tex 报告
- 线性拟合等数学处理

## Install 安装

1. `pip`安装：

```shell
pip install -U autolatex
```

如果更换过镜像源，版本更新可能会不及时，请检查安装版本是否最新 [![PyPI](https://img.shields.io/pypi/v/autolatex)](https://pypi.org/project/autolatex/)  
若镜像源没有及时更新，建议临时切换为官方源

```shell
pip install -U autolatex -i https://pypi.org/simple
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
   import pandas as pd

   df = pd.read_excel('data.xlsx')
   output = table.convert(df)
   print(output)
   ```

3. word2tex  
   详见`word2tex`下的 [README](autolatex/word2tex/README.md)
