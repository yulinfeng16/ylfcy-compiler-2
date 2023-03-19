def examplemod():
    return 0
def cutstring(code,x,y):
    strs=""
    for i in range(x,y):
        strs+=code[i]
    return strs
def checkCDC(weixy):
    if weixy.find('类型')==-1:
        return -1
    elif weixy.count('类型')>1:
        return -2
    return 0
def customdefineconv(code,ln):
    retstr=''
    if checkCDC(cutstring(code,0,int(code.find('为'))))==-2:
        raise SyntaxError('“定义*类型”不能重复附加更多类型。（位于第'+str(ln)+'行）')
    u=code.find('类型')
    lxstr=''
    for i in range(2,u):
        lxstr+=code[i]
    if lxstr=='整型':
        retstr+='int '
    elif lxstr=='浮点':
        retstr+='float '
    elif lxstr=='双精':
        retstr+='double '
    elif lxstr=='字符串':
        retstr+='string '
    elif lxstr=='字符':
        retstr+='char '
    elif lxstr=='长整型':
        retstr+='long long '
    elif lxstr=='短整型':
        retstr+='short '
    else:
        raise ValueError("发现意外的变量类型。"+'(位于第'+str(ln)+'行第'+'3'+'个字符)')
    return retstr
