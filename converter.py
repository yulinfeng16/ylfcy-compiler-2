#-*-coding:gbk-*-
import sys
if __name__=="__main__":
    cpp_buffer=['//由YLFCY COMPILER转换！','#include<iostream>','#include<cmath>','#include<ctime>','#include<string>','#include<cstring>','#include<algorithm>','#include<vector>','#include<queue>','using namespace std;']
    #头文件和初始化
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("接收到："+cpiurl)
    with open (cpiurl,encoding='UTF8') as file_object:
        lines=file_object.readlines()#读取文件内容
    code_string=''#初始化
    for line in lines:
        code_string=line.rstrip()
        print(code_string)
        #以下为分析文件内容并转换为C++代码
        
    print("读取成功！")
    with open ('out.cpp','w',encoding='ANSI') as file_object2:
        for line in cpp_buffer:
            file_object2.write(line+'\n')#将转换好的代码写入文件
    print('写入完毕！')
