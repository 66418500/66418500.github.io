#!/bin/sh
#Auther: huangguinan
#Time: 2021/09/08
#email: 3481203724@qq.com

#This script is used to automatically generate article content and upload it to my Github Pages space.
#When code is pushed to the blog branch, Github actions are automatically built to deploy the generated public directory to the Master branch.
set -e


geneNewArchives(){
  content=`fortune`
  title=`echo $content|awk 'NR==1{print $1}'|tr -dc '[:alnum:]'`  #Just assume that the first field on the first line of the article is the title, with the symbol removed
  hugo new post/$title.md
  echo $content >> content/post/$title.md
  sed -i 's/draft: true/draft: false/g' content/post/$title.md 
  
  if [ ! -d "themes/jane/layouts" ];then #Jane is also a Git repository, so it is not uploaded, and you will need to reinstall the theme if you use it for the first time
    git clone https://github.com/xianmin/hugo-theme-jane.git --depth=1 themes/jane
  fi
  
  hugo -t jane # if using a theme, replace with `hugo -t <YOURTHEME>`
}

pushTorepo(){
  git add .
  msg="the new archive updating. $(date)"
  git commit -m "$msg" && git push origin blog
  }


geneNewArchives
pushTorepo
