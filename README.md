# AutoLaTeX

[Github地址](https://github.com/Benature/AutoLaTeX)

Generate LaTeX code by Python for experiment report.

用Python生成LaTeX代码写实验报告。  

## Features 特性

- 读取excel等表格文件转为latex表格
- 线性拟合等数学处理
- (假的)word讲义转tex报告

## Install 安装

1. `pip`安装：

```shell
pip install -U autolatex
```

2. 源码使用

```shell
git clone git@github.com:Benature/AutoLaTeX.git
```

## Usage 使用

1. `.py`文件内
```python
import autolatex as alt
```

2. `xlsx`文件 excel 表格数据转 tex 代码
  在命令行输入（两种写法等效）：
  ```shell
  autolatex --f <文件路径>
  alt --f <文件路径>
  ```

3. word2tex
   详见`word2tex`下的 README

---

>如果有帮助就点个star呗  
>欢迎 Pull Request, Fork, 提 issue.
