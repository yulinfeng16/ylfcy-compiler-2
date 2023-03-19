#-*-coding:gbk-*-
import sys
import re
from tqdm import tqdm
from addmodule01 import examplemod,customdefineconv,checkCDC,cutstring
def coutconv(code_stream,j):
    cout_str='cout<<'
    if code_stream[len(code_stream)-1]=='“' or code_stream[len(code_stream)-1]=='，':
        raise ValueError('错误的行结尾:'+code_stream[len(code_stream)-1]+'(位于第'+str(j)+'行第'+str(len(code_stream))+'个字符)')
    if len(code_stream)<3:
        raise SyntaxError("“输出”至少要附加一个内容(位于第"+str(j)+"行)")
    i=2
    while i<len(code_stream):
        #print(code_stream[i])
        if code_stream[i]=='“' or code_stream[i]=='”':
            cout_str+='"'
        elif code_stream[i]=='‘' or code_stream[i]=='’':
            cout_str+='\''
        elif code_stream[i]=='换' and code_stream[i+1]=='行':
            cout_str+='endl'
            i+=1
        elif code_stream[i]=='，':
            cout_str+='<<'
        else:
            cout_str+=code_stream[i]
        i+=1
    cout_str+=';'
    return cout_str
def checkADC(code):
    for i in range(3,len(code)-1):#保证有且最后不是“为”
        if code[i]=='为':
            return False
    return True
def autodefineconv(code,ln):
    retstr='auto '
    if(checkADC(code)):
        raise SyntaxError('“定义”至少要附加一个变量名和一个值。您是否在找“定义*类型”？（位于第'+str(ln)+"行)")
    z=code.find('为')
    for i in range(2,z):
        retstr+=code[i]
    for i in range(z,len(code)):
        if code[i]=='“' or code[i]=='”':
            retstr+='"'
        elif code[i]=='‘' or code[i]=='’':
            retstr+='\''
        elif code[i]=='为':
            retstr+='='
        else:
            retstr+=code[i]
    retstr+=';'
    return retstr
if __name__=="__main__":
    print("辅助模块自检返回："+str(examplemod()))
    cpp_buffer=['//由YLFCY COMPILER转换！','#include<iostream>','#include<cmath>','#include<ctime>','#include<string>','#include<cstring>','#include<algorithm>','#include<vector>','#include<queue>','using namespace std;','int main(){']
    #头文件和初始化
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("接收到："+cpiurl)
    with open (cpiurl,encoding='UTF8') as file_object:
        lines=file_object.readlines()#读取文件内容
    code_string=''
    out_buffer=''#初始化
    summ=0
    flag=False
    print(len(lines))
    with tqdm(total=len(lines)) as pbar:
        for line in lines:
            flag=True
            summ+=1
            pbar.set_description('正在转换')
            code_string=line.rstrip()
            #print(code_string)
            #以下为分析文件内容并转换为C++代码
            if len(code_string)==0:
                pass
            elif re.match("输出",code_string)!=None:
                out_buffer=coutconv(code_string,summ)
            elif re.match("定义",code_string)!=None and checkCDC(cutstring(code_string,0,int(code_string.find('为'))))==-1:
                out_buffer=autodefineconv(code_string,summ)
            elif re.match("定义",code_string)!=None and checkCDC(cutstring(code_string,0,int(code_string.find('为'))))==0:
                out_buffer=customdefineconv(code_string,summ)
            else:
                raise SyntaxError("未知指令(第"+str(summ)+"行)")
            if flag:
                cpp_buffer.append(str(out_buffer))
            pbar.update(1)
    cpp_buffer.append('return 0;}')
    print("转换成功！")
    with open ('out.cpp','w',encoding='ANSI') as file_object2:
        for line in cpp_buffer:
            file_object2.write(line+'\n')#将转换好的代码写入文件
    print('写入完毕！')
    print(cpp_buffer)
