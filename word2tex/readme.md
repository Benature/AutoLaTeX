# Word2Tex

说`Word2Tex`其实有点标题党, 实际上是先用`pandoc`将`.docx`转为`.tex`, 再将原始的`.tex`文件内容修改为更符合实验报告的形式.

>有了[瑞士军刀](https://pandoc.org/)干嘛还造轮子呢

## 说在前头

1. **本程序仅为减轻实验报告的** ***非动脑时间负担*** **, 请认真阅读实验报告并独立思考, 不提倡无脑复制!**
2. pandoc的`.word`转`.tex`效果还是挺差的, 请勿过度依赖.
3. 能力有限, 代码粗陋, 欢迎PR.
4. 还有需求或其他意见欢迎提issue.

## Usage

1. [pandoc](https://pandoc.org/)

    ```shell
    pandoc '.\lecture.docx' -o report.tex --extract-media="./"
    ```

    其中`--extract-media`参数设置导出媒体文件(如图片)夹的路径, 不设置不导出

2. configuration

    将`config_sample.py`文件改名为`config.py`, 然后修改里面的配置项.

3. run python

    ```shell
    python3 word2tex.py
    ```

4. **手动修改**

>如果觉得有帮助还请点个Star吧 :)

## TODO List

- [ ] 优化figure的caption匹配
- [ ] 优化公式字母的处理
- [ ] 支持自定义导言区
- [ ] 用`os`处理文件路径
- [ ] 函数说明/文档
