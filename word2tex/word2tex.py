import re
from config import *
from modify_re import *

with open(tex_raw_path, "r") as f:
    tex_content = f.read()

# for item in ["\\begin{quote}", "\\end{quote}"]:
#     tex_content = tex_content.replace(item, "")

tex_content = clean_useless(tex_content)
tex_content = re.sub(r"\\begin{longtable}.*?\\end{longtable}", modify_re_table, tex_content, flags=re.DOTALL)
tex_content = re.sub(r"\n.*?【.*?】.*?\n", modify_re_section, tex_content)
tex_content = modify_figure(tex_content, policy="manual")[0]

with open(tex_out_path, "w") as f:
    f.write(template_document.format(
        get_exp_title(tex_content), tex_content)
    )

