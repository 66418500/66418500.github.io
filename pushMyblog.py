#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import subprocess
import os
import random

def initTheme():
    jane = '/themes/jane/.git'
    if not os.path.exists(jane): #Jane is also a repository and won't be uploaded to Github, so you'll need to reinstall the theme for the first time.
        os.system('git clone https://github.com/xianmin/hugo-theme-jane.git --depth=1 themes/jane')

def main():
    content = subprocess.getstatusoutput('fortune')
    if content[0]!=0:
        print('Check whether the command fortune has been installed.')

    if content[0]==0:
        title="MyPost"+str(random.randint(0,1000))
        try:
            os.system('hugo new post/{0}'.format(title))
            with open('content/post/{0}'.format(title), 'r+') as f: #r+ reading and writing
                file=f.read()
                file=file.replace('draft: true','draft: false')
                f.seek(0) #Initialize the position to the beginning
                f.write(file)
                f.write(content[1])
            os.system('hugo  -t jane')
            os.system('git add .')
            msg='the new archive updatingdate {0})'.format(title)
            os.system('git commit -m "{0}" && git push origin blog'.format(msg))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    #initTheme() #if you're first use this scripts,please excute this function first.
    main()
        