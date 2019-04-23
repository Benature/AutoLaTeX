def isFloat(num):
    if "float" in str(type(num)):
        return True  
    else: 
        return False

def write_table(df, typ = "tex", ilim=None, jlim=None):
    '''
    df: dateframe
    
    typ: type of output. "md" or "latex"/"tex".   
        Default as "tex"

    ilim: row limits. Can be stop or (begin, stop)
    
    jlim: vol limits. Can be stop or (begin, stop)
    '''
    header = list(df.columns)
    IN, JN = df.shape
    I0, J0, In, Jn = 0, 0, IN, JN
    if (ilim):
        try:
            In = int(ilim)
        except:
            I0, In = ilim
        I0 = IN+I0 if (I0<0) else I0
        In = IN+In if (In<=0) else In
    if (jlim):
        try:
            Jn = int(jlim)
        except:
            J0, Jn = jlim
        J0 = JN+J0 if (J0<0) else J0
        Jn = JN+Jn if (Jn<=0) else Jn
        print(J0, Jn)


    if typ == "md":
        out = "|" + "|".join(["{:^7}".format(h) for h in header]) + "|"
        for i in range(In):
            out += "\n|"
            for j in range(Jn):
                out += "{:^7}|".format((df.iloc[i][j])) if (header[j]=="index") \
                        else  "{:^7}|".format(df.iloc[i][j])


    elif typ == "latex" or typ =="tex":
        out = '''
\\begin{table}[htbp]
\t\\centering
\t\\scalebox{1}{
\t\t\\begin{tabular}[c]{''' \
+ "".join(["c"]*(Jn-J0)) + \
'''}
\t\t\t\\toprule[1.5pt]
\t\t\t'''
        out += "&".join(["{:^7}".format(h) for h in header][J0:Jn])
        out += "\\\\ \n\t\t\t\\midrule[1pt] \n\t\t\t"
        for i in range(I0, In):
#             out += "\\\\ \n"
            for j in range(J0, Jn):
                item = df.iloc[i][j]
#                 print(type(item), item)
                if (header[j]=="index"):
                    out += " {:^7} &".format(item)
                elif (isFloat(item)):
#                     print(item)
                    out += " {:.4f} &".format(item)
                else:  
                    out += " {:^7} &".format(item)
            out = out[:-1] + "\\\\ \n\t\t\t"
        out = out[:-4] + '''
\t\t\t\\bottomrule[1.5pt]
\t\t\\end{tabular}
\t}
%\t\\caption{}
%\t\\label{t:}
\\end{table}
'''


    else:
        out = "Wrong Type!!!"
    return out
    
    