#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#auther: huangguinan
#time: 2021/09/09
#email: 3481203724@qq.com

#This script is used to automatically generate article content and upload it to my Github Pages space.
#When code is pushed to the blog branch, Github actions are automatically built to deploy the generated public directory to the Master branch.

import subprocess
import os
import random

def main():
    content = subprocess.getstatusoutput('fortune') 
    #The subprocess module returns two parameters, the execution status of the command and the content, exception if the status is not zero.
    if content[0]!=0: 
        print('Check whether the command fortune has been installed.')
    if content[0]==0:
        title="MyPost"+str(random.randint(0,1000)) 
        try:
            os.system('hugo new post/{0}.md'.format(title))  #There is no need to get the return content, so use the OS module directly
            with open('content/post/{0}.md'.format(title), 'r+') as f: #r+ reading and writing
                file=f.read()
                file=file.replace('draft: true','draft: false')
                f.seek(0) #Initialize the position to the beginning
                f.write(file)
                f.write(content[1])
            
            if not os.path.isdir("themes/jane/layouts"): #Jane is also a repository and won't be uploaded to Github, so you'll need to reinstall the theme for the first time.
                os.system('git clone https://github.com/xianmin/hugo-theme-jane.git --depth=1 themes/jane')
            os.system('hugo  -t jane')
            os.system('git add .')
            msg='the new archive updatingdate {0})'.format(title)
            os.system('git commit -m "{0}" && git push origin blog'.format(msg))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
        
