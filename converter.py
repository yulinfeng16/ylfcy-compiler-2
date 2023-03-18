#-*-coding:UTF-8-*-
import sys
if __name__=="__main__":
    cpiurl="init"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("接收到："+cpiurl)
    with open (cpiurl) as file_object:
