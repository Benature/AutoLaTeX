'''
It is part of .py file of word2tex
'''

from .config import stid, major, grade, name, preamble

# ========== table ==========

template_table = '''
\\begin{{table}}[htbp]
    \\centering
    %\\caption{{}}
    %\\label{{t:}}
    \\scalebox{{1}}{{
    \\begin{{tabular}}[c]{}
{}
    \\end{{tabular}}
    }}
\\end{{table}}
'''

# ========== figure ==========

template_figure = '''
\\begin{{figure}}[htbp]
    \\setcaptionwidth{{0.5\\textwidth}}
    \\centering 
    {}
    \\caption{{}}
    \\label{{f:tu}}
\\end{{figure}}
'''

preamble = preamble.replace("{", "{{").replace("}", "}}")

template_document = preamble + '''
\\newcommand{{\\exptitle}}{}
\\newcommand{{\\stid}}{{''' + stid + '''}}
\\newcommand{{\\major}}{{''' + major + '''}}
\\newcommand{{\\grade}}{{''' + grade + '''}}
\\newcommand{{\\name}}{{''' + name + '''}}

\\begin{{document}}
{}
\\end{{document}}
'''


Unicode2Latex = {
    "α": "alpha",
    "∝": "alpha",
    "𝜋": "pi",
    "𝑑": "mathrm{d}",
    "∆": "Delta",
    "∫": "int",
    "×": "times",
    "ρ": "rho",
    "Ω": "Omega",
    "·": "cdot",
    "→": "rightarrow",
    "Σ": "Sigma",

}

Unicode2Unicode = {
    "°": "^\\circ",
    "𝐸": "E",
    "𝑣": "v",
    "𝑁": "N",
    "𝑍": "Z",
    "𝑒": "e",
    "𝐴": "A",
    "𝐻": "H",
}
