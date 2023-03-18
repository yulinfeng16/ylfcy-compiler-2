#-*-coding:gbk-*-
import sys
import re
def coutconv(code_stream,j):
    cout_str='cout<<'
    if code_stream[len(code_stream)-1]=='“' or code_stream[len(code_stream)-1]=='，':
        raise ValueError('错误的行结尾:'+code_stream[len(code_stream)-1]+'(位于第'+str(j)+'行第'+str(len(code_stream))+'个字符)')
    for i in range(3,len(code_stream)):
        if code_stream[i]=='“' and code_stream:
            cout_str+='<<'
    cout_str+=';'
    return cout_str
if __name__=="__main__":
    cpp_buffer=['//由YLFCY COMPILER转换！','#include<iostream>','#include<cmath>','#include<ctime>','#include<string>','#include<cstring>','#include<algorithm>','#include<vector>','#include<queue>','using namespace std;']
    #头文件和初始化
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("接收到："+cpiurl)
    with open (cpiurl,encoding='UTF8') as file_object:
        lines=file_object.readlines()#读取文件内容
    code_string=''
    out_buffer=''#初始化
    sum=0
    for line in lines:
        sum+=1
        code_string=line.rstrip()
        print(code_string)
        #以下为分析文件内容并转换为C++代码
        if re.match("输出“",code_string)!=None:
            out_buffer=coutconv(code_string,sum)
        cpp_buffer+=out_buffer    
    print("读取成功！")
    with open ('out.cpp','w',encoding='ANSI') as file_object2:
        for line in cpp_buffer:
            file_object2.write(line+'\n')#将转换好的代码写入文件
    print('写入完毕！')
