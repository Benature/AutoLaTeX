def write_table(df, typ = "tex"):
    '''
    df: 
    dateframe.
    
    typ: 
    type of output. "md" or "latex"/"tex".
    default as "tex"

    output:
    number will be float if its head is not "index".
    '''
    header = list(df.columns)
    In, Jn = df.shape
    if typ == "md":
        out = "|" + "|".join(["{:^7}".format(h) for h in header]) + "|"
        for i in range(In):
            out += "\n|"
            for j in range(Jn):
                out += "{:^7}|".format(int(df.iloc[i][j])) if (header[j]=="index") \
                        else  "{:^7}|".format(df.iloc[i][j])
    elif typ == "latex" or typ =="tex":
        out = '''
\\begin{table}[htbp]
\t\\centering
\t\\scalebox{1}{
\t\t\\begin{tabular}[c]{ccc}
\t\t\t\\toprule[1.5pt]
\t\t\t'''
        out += "&".join(["{:^7}".format(h) for h in header])
        out += "\\\\ \n\t\t\t\\midrule \n\t\t\t"
        for i in range(In):
#             out += "\\\\ \n"
            for j in range(Jn):
                out += "{:^7}&".format(int(df.iloc[i][j])) if (header[j]=="index") \
                        else  "{:^7}&".format(df.iloc[i][j])
            out = out[:-1] + "\\\\ \n\t\t\t"
        out = out[:-4] + '''
\t\t\\end{tabular}
\t}
%\t\\caption{}
%\t\\label{t:}
\\end{table}
'''
    else:
        out = "Wrong Type!!!"
    print(out)