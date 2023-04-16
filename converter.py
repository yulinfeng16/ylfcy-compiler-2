#-*-coding:gbk-*-
import sys
import re
from tqdm import tqdm
from modules.libext.addmodule01 import examplemod,customdefineconv,checkCDC,cutstring
from modules.libext.stringcz01 import reversed_string
def coutconv(code_stream,j):
    cout_str='cout<<'
    if code_stream[len(code_stream)-1]=='��' or code_stream[len(code_stream)-1]=='��':
        raise ValueError('������н�β:'+code_stream[len(code_stream)-1]+'(λ�ڵ�'+str(j)+'�е�'+str(len(code_stream))+'���ַ�)')
    if len(code_stream)<3:
        raise SyntaxError("�����������Ҫ����һ������(λ�ڵ�"+str(j)+"��)")
    i=2
    while i<len(code_stream):
        #print(code_stream[i])
        if code_stream[i]=='��' or code_stream[i]=='��':
            cout_str+='"'
        elif code_stream[i]=='��' or code_stream[i]=='��':
            cout_str+='\''
        elif code_stream[i]=='��' and code_stream[i+1]=='��':
            cout_str+='endl'
            i+=1
        elif code_stream[i]=='��':
            cout_str+='<<'
        else:
            cout_str+=code_stream[i]
        i+=1
    cout_str+=';'
    return cout_str
def checkADC(code):
    for i in range(3,len(code)-1):#��֤��������ǡ�Ϊ��
        if code[i]=='Ϊ':
            return False
    return True
def autodefineconv(code,ln):
    retstr='auto '
    if(checkADC(code)):
        raise SyntaxError('�����塱����Ҫ����һ����������һ��ֵ�����Ƿ����ҡ�����*���͡�����λ�ڵ�'+str(ln)+"��)")
    z=code.find('Ϊ')
    for i in range(2,z):
        retstr+=code[i]
    for i in range(z,len(code)):
        if code[i]=='��' or code[i]=='��':
            retstr+='"'
        elif code[i]=='��' or code[i]=='��':
            retstr+='\''
        elif code[i]=='Ϊ':
            retstr+='='
        else:
            retstr+=code[i]
    retstr+=';'
    return retstr
def retconv(code):
    retstr='return '
    for i in range(2,len(code)):
        if code[i]=='��' or code[i]=='��':
            retstr+='"'
        elif code[i]=='��' or code[i]=='��':
            retstr+='\''
        elif code[i]=='Ϊ':
            retstr+='='
        else:
            retstr+=code[i]
    retstr+=';'
    return retstr
def whiconv(code):
    retstr='while('
    for i in range(4,len(code)-3):
        if code[i]=='��' or code[i]=='��':
            retstr+='"'
        elif code[i]=='��' or code[i]=='��':
            retstr+='\''
        elif code[i]=='Ϊ':
            retstr+='='
        else:
            retstr+=code[i]
    retstr+=')'
    return retstr
def convert000(code,ln):
    retstr=''
    if(checkADC(code)):
        raise SyntaxError('���޸ġ�����Ҫ����һ����������һ��ֵ����λ�ڵ�'+str(ln)+"��)")
    z=code.find('Ϊ')
    for i in range(2,z):
        retstr+=code[i]
    for i in range(z,len(code)):
        if code[i]=='��' or code[i]=='��':
            retstr+='"'
        elif code[i]=='��' or code[i]=='��':
            retstr+='\''
        elif code[i]=='Ϊ':
            retstr+='='
        else:
            retstr+=code[i]
    retstr+=';'
    return retstr
if __name__=="__main__":
    print("����ģ���Լ췵�أ�"+str(examplemod()))
    cpp_buffer=['//��YLFCY COMPILERת����','#include<iostream>','#include<cmath>','#include<ctime>','#include<string>','#include<cstring>','#include<algorithm>','#include<vector>','#include<queue>','using namespace std;','int main(){']
    #ͷ�ļ��ͳ�ʼ��
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("���յ���"+cpiurl)
    with open (cpiurl,encoding='UTF8') as file_object:
        lines=file_object.readlines()#��ȡ�ļ�����
    code_string=''
    out_buffer=''#��ʼ��
    summ=0
    flag=False
    print(len(lines))
    with tqdm(total=len(lines)) as pbar:
        for line in lines:
            flag=True
            summ+=1
            pbar.set_description('����ת��')
            code_string=line.rstrip()
            #print(code_string)
            #����Ϊ�����ļ����ݲ�ת��ΪC++����
            if len(code_string)==0:
                pass
            elif code_string=="{" or code_string=="}":
                out_buffer=code_string;
            elif re.match("���",code_string)!=None:
                out_buffer=coutconv(code_string,summ)
            elif re.match("����",code_string)!=None and checkCDC(cutstring(code_string,0,int(code_string.find('Ϊ'))))==-1:
                out_buffer=autodefineconv(code_string,summ)
            elif re.match("����",code_string)!=None and checkCDC(cutstring(code_string,0,int(code_string.find('Ϊ'))))==0:
                out_buffer=customdefineconv(code_string,summ)
            elif re.match("����",code_string)!=None:
                out_buffer=retconv(code_string)
            elif re.match("ѭ��ֱ��",code_string)!=None and re.match("���ɲ�",reversed_string(code_string))!=None:
                out_buffer=whiconv(code_string)
            elif re.match("�޸�",code_string)!=None:
                out_buffer=convert000(code_string,summ)
            elif code_string=="��ͣ":
                out_buffer="system(\"pause\");"
            else:
                print(code_string,"<-")
                raise SyntaxError("δָ֪��(��"+str(summ)+"��)")
            if flag:
                cpp_buffer.append(str(out_buffer))
            pbar.update(1)
    cpp_buffer.append('}')
    print("ת���ɹ���")
    with open ('out.cpp','w',encoding='ANSI') as file_object2:
        for line in cpp_buffer:
            file_object2.write(line+'\n')#��ת���õĴ���д���ļ�
    print('д����ϣ�')
    print(cpp_buffer)
