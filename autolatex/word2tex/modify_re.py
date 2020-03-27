import re
from .templates import *

delete_list = ["\\begin{quote}", "\\end{quote}"]
delete_table_list = ["\\end{minipage}",
                     "\\raggedright", "\\strut", "\\endhead"]


def modify_re_table(table):
    r'''render table'''
    table = table.group()
    for li in delete_table_list:
        table = table.replace(li, "")
    table = re.sub(
        r"\\begin{minipage}.*?{.*?\\columnwidth}", "", table, flags=re.DOTALL)
    table = re.sub(r"\n *\n", "", table, flags=re.DOTALL)
    table = re.sub(r"^\\begin{.*?}.*?\n", "", table, flags=re.DOTALL)
    table = re.sub(r"\\end{.*?}.*?$", "", table, flags=re.DOTALL)

    table = re.sub(r"\n* *& *\n*", " & ", table, flags=re.DOTALL)
    table = table.replace("\\tabularnewline", "\\\\")  # 换行
    table = re.sub(r"\n*\\\\\n*", "\\\\\\\n", table, flags=re.DOTALL)
    table = re.sub(r"\\toprule\n*",
                   r"\\toprule[1.5pt]\n", table, flags=re.DOTALL)
    table = re.sub(r"\\midrule\n*",
                   r"\\midrule[1pt]\n", table, flags=re.DOTALL)
    table = re.sub(r"\\bottomrule\n*",
                   r"\\bottomrule[1.5pt]\n", table, flags=re.DOTALL)

    row_n = list(re.search(r"\n.*?&.*?\n", table,
                           flags=re.DOTALL).group()).count("&")
    table = template_table.format("{"+"c"*row_n+"c}", table)
    return table


def modify_re_section(section):
    r'''render \section{}'''
    section = section.group()
    section = re.findall(r"(?=【).*?(?<=】)", section)[0]
    section = section.strip("【】")  # 蜜汁bug
    # print(section)
    return "\n\\section{" + section + "}"


def modify_re_figure(figure):
    figure = figure.group()
    return template_figure.format(figure)


def modify_figure(tex_raw, policy="donot"):
    '''
    policy: 对于title的处理策略
      ["donot"(default), "manual", "close"]
    '''
    if policy == "donot":
        tex_raw = re.sub(r"\\includegraphics.*?}", modify_re_figure, tex_raw)
        return tex_raw, "不删除题目", None
    if policy == "manual":
        tex_raw = re.sub(r"\\includegraphics.*?}", modify_re_figure, tex_raw)
        titles = re.findall(
            r"\n.*?[^\u4e00-\u9fa5，。、]图 *?\d ..*?\n", tex_raw)  # "图"前非中文及部分标点
        for title in titles:
            print(title.replace("\n", ""))
            tex_raw = tex_raw.replace(title, "")
        return tex_raw, "手动模式", titles
    if policy == "close":  # 就近原则
        figure_li = re.findall(r"\\includegraphics.*?}", tex_raw)
        for graphics in figure_li:
            re_title = re.compile(r"%s(?:.|\n)*?图 *?\d.*?\n" %
                                  ("\\"+graphics.replace("[", r"\[").replace("]", r"\]")))
            find_title = re_title.findall(tex_raw)
            if len(find_title) == 1:
                find_title = find_title[0]
                if len(re.findall(r"includegraphics", find_title)) == 1:
                    title = re.findall(
                        r"图 *?\d.*?\n", find_title)[0].replace("\n", "")
                    tex_raw = tex_raw.replace(graphics, template_figure.format(
                        graphics, "{"+title+"}"))
                    tex_raw = tex_raw.replace(title, "{{}}")
                    continue
            tex_raw = tex_raw.replace(
                graphics, template_figure.format(graphics, "{}"))
        return tex_raw, "就近原则", None


def get_exp_title(tex_raw):
    '''get title'''
    # exp_title = re.findall(r"实验 \w\d.*?\n", tex_raw)[0].rstrip("}\n")
    exp_title = re.findall(r"实验 .*\d.*?\n", tex_raw)[0].rstrip("}\n")
    print("Titile | ", exp_title)
    return "{" + exp_title + "}"


def clean_useless(tex_raw):
    for item in delete_list:
        tex_raw = tex_raw.replace(item, "")
    for i in re.findall(r"\\hypertarget.*", tex_raw):
        print(i)
        tex_raw = tex_raw.replace(i, "\n")
    tex_raw = re.sub(r"\\hypertarget.*", "\n", tex_raw)
    return tex_raw


def modify_re_math(math):
    math = math.group()
    return "$" + math.lstrip("\\emph{").rstrip("}").replace("$", "") + "$"


def math_latex(tex_raw):
    for u, l in zip(Unicode2Latex.keys(), Unicode2Latex.values()):
        tex_raw = tex_raw.replace(u, "$\\"+l+"$")
    for u, l in zip(Unicode2Unicode.keys(), Unicode2Unicode.values()):
        tex_raw = tex_raw.replace(u, ""+l+"")
    tex_raw = re.sub(r"\\emph{.*?}", modify_re_math, tex_raw)

    # tex_raw = re.sub(r"\$[ ]*\$", "", tex_raw)
    return tex_raw
