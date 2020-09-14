# ===================== 路径配置 ============================

folder_path = "folder/path/"
tex_raw_path = folder_path + "raw.tex"
tex_out_path = folder_path + "out.tex"


# ================== 实验报告表头信息 ============================

stid = "173530xx"
major = "物理学"
grade = "17级"
name = "木一"


# ================== tex 导言区设置 ============================
# 推荐使用 StarHub 设计好的实验模板 (链接如下)
# https://github.com/StarHub-SPA/Experiment_Report_SPA_Template

preamble = '''
\\documentclass[no-math,zihao = -4]{ctexart}
\\usepackage{"../../Experiment_Report_SPA_Template/loeng's_taste/spaexptemp"} 
'''
