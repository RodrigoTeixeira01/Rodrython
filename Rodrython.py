import sys
var=[]
def executar(code,sep=";",varc=100,onTry=False):
    global var
    try:
        code=code.replace("\\n","\n")
        code="".join(code.split("#")[::2])
        funcn=[]
        funcv=[]
        for a in range(varc):
            var.append("")
        def cmc_em(string,stringcmc):
            if string[:len(stringcmc)]==stringcmc:
                return True
            return False
        def vfunc(funkn,funcn,funcv):
            for a in range(len(funcn)):
                if funcn[a] == funkn:
                    return funcv[a]
        def syntaxError(msg="SyntaxError"):
            print("" if onTry else msg)
        for a in code.split(sep):
            for z in range(len(var)):
                a=a.replace(str(z)+"\\"+str(z),var[z])
            a=a.replace("c\\c",",")
            a=a.replace("pc\\pc",";")
            a=a.replace("p\\p","#")
            a=a.replace("\\\\","\\")
            if cmc_em(a,"\n"):
                a=a[1:]
            a=a.lstrip()
            if cmc_em(a,"define "):
                if ":" in a:
                    funcn.append(a[7:a.find(":")])
                    funcv.append(a[a.find(":")+1:])
                else:
                    syntaxError()
                    return 0
            elif cmc_em(a,"execute "):
                executar(vfunc(a[8:],funcn,funcv),",")
            elif cmc_em(a,"print "):
                print(a[6:],end="")
            elif cmc_em(a,"input "):
                var[0]=input(a[6:])
            elif a=="input":
                var[0]=input("")
            elif cmc_em(a,"if "):
                a=a[3:]
                if "=" in a:
                    if ":" in a.split("=")[1]:
                        if a.split(":")[0].split("=")[0]==a.split(":")[0].split("=")[1]:
                            executar("".join(a.split(":")[1:]),",")
                    else:
                        syntaxError()
                        return 0
                else:
                    syntaxError()
                    return 0
            elif cmc_em(a,"var "):
                if a.split()[1].split("=")[0].isnumeric():
                    var[int(a.split()[1].split("=")[0])]="=".join(a.split("=")[1:])
                else:
                    syntaxError()
                    return 0
            elif cmc_em(a,"add "):
                try:
                    var[0]=str(int(a.split()[1])+int(a.split()[2]))
                except:
                    syntaxError()
            elif cmc_em(a,"while "):
                a=a[6:]
                if "=" in a:
                    if ":" in a.split("=")[1]:
                        while a.split(":")[0].split("=")[0]==a.split(":")[0].split("=")[1]:
                            executar("".join(a.split(":")[1:]),",")
                    else:
                        syntaxError()
                        return 0
                else:
                    syntaxError()
                    return 0
            elif cmc_em(a,"repeat "):
                if a[7:a.find(":")].isnumeric():
                    for cc in range(int(a[7:a.find(":")])):
                        executar(a[a.find(":")+1:],",")
                else:
                    syntaxError()
                    return 0
            elif cmc_em(a,"try:"):
                try:
                    executar(a[4:],",",onTry=True)
                except:
                    passz
            elif cmc_em(a,"//") or a == "":
                continue
            elif a in ("break","exit"):
                return 0
            else:
                syntaxError()
                return 0
    except:
        syntaxError("Error")
        return 0
if len(sys.argv)>1:
    executar(" ".join(sys.argv[1:]))
else:
    try:
        loc=input("")
        executar(open(loc if loc[-4:]==".rod" else ".").read())
    except:
        if type(executar(loc))==type(None):
            while type(executar(input("")))==type(None):
                pass
