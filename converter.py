#-*-coding:UTF-8-*-
import sys
if __name__=="__main__":
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("接收到："+cpiurl)
    with open (cpiurl) as file_object:
        lines=file_object.readlines()
    print(lines)
