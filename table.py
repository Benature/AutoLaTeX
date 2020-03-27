import pandas as pd
from platform import system

SYSTEM = system()

read_excel = pd.read_excel

def isFloat(num):
    if "float" in str(type(num)):
        return True
    else:
        return False

def setClipboardData(str):
    if SYSTEM == 'Darwin':
        import subprocess
        data = bytes(str,'utf8')
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.stdin.write(data)
        p.stdin.close()
        p.communicate()
    elif SYSTEM == 'Windows':
        import pyperclip
        pyperclip.copy(str)
    

def convert(df, typ="tex", ilim=None, jlim=None, clipboard=True,
            border='|', hline=True, caption='实验数据：'):
    '''
    df: dateframe

    typ[str]: type of output. "md" or "latex"/"tex".   
        Default as "tex"

    ilim[list]: row limits. Can be stop or (begin, stop)

    jlim[list]: vol limits. Can be stop or (begin, stop)

    clipboard[bool]: auto send text to clipboard

    border[str]: tex mode, set the table border. 
        Default as "|"
    
    hline[bool, str]: tex mode, set the table border. 
        Default as True

    caption[str]: tex mode, set the table caption.
        Default as "实验数据："
    '''
    df = df.fillna('')  # clean data
    header = list(df.columns)
    IN, JN = df.shape
    I0, J0, In, Jn = 0, 0, IN, JN
    if (ilim):
        try:
            In = int(ilim)
        except:
            I0, In = ilim
        I0 = IN+I0 if (I0 < 0) else I0
        In = IN+In if (In <= 0) else In
    if (jlim):
        try:
            Jn = int(jlim)
        except:
            J0, Jn = jlim
        J0 = JN+J0 if (J0 < 0) else J0
        Jn = JN+Jn if (Jn <= 0) else Jn
        print(J0, Jn)

    if typ == "md":
        out = "|" + "|".join(["{:^7}".format(h) for h in header]) + "|"
        for i in range(In):
            out += "\n|"
            for j in range(Jn):
                out += "{:^7}|".format((df.iloc[i][j])) if (header[j] == "index") \
                    else "{:^7}|".format(df.iloc[i][j])

    elif typ == "latex" or typ == "tex":
        if hline == True:
            hline = '\\hline'
        elif hline == False:
            hline = ''
        # user can config their own hline
        out = f'''\\begin{{table}}[htbp]
    \\centering
    \\caption{{{caption}}}
    \\label{{t:}}
    \\scalebox{{1}}{{
        \\begin{{tabular}}[c]{{{border}''' \
    + border.join(["c"]*(Jn-J0)) +\
            f'''{border}}}
            \\toprule[1.5pt]
            '''
        out += "& ".join(["{:^7}".format(h) for h in header][J0:Jn])
        out += "\\\\ \n\t\t\t\\midrule[1pt] \n\t\t\t"
        for i in range(I0, In):
            for j in range(J0, Jn):
                item = df.iloc[i][j]
                if (header[j] == "index"):
                    out += " {:^7} &".format(item)
                elif (isFloat(item)):
                    out += " {:.4f} &".format(item)
                elif item == "":
                    out += "&"
                else:
                    out += " {:^7} &".format(item)
            out = out[:-1] + "\\\\ " + hline + "\n\t\t\t"
        out = out[:-4] + '''
            \\bottomrule[1.5pt]
        \\end{tabular}
    }\n\\end{table}'''
        if clipboard:
            try:
                setClipboardData(out)
            except Exception as e:
                print("复制到剪贴板失败！", e)

    else:
        out = "Wrong Type!!!"
    return out
