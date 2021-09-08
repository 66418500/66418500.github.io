#!/bin/sh
#Auther: huangguinan
#Time: 2021/09/08
#This script is used to automatically generate article content and upload it to my Github Pages page.
set -e

geneNewArchives(){
  content=`fortune`
  title=`echo $content|awk 'NR==1{print $1}'|tr -dc '[:alnum:]'`
  hugo new post/$title.md
  echo $content >> content/post/$title.md
  sed -i 's/draft: true/draft: false/g' content/post/$title.md
}

pushTorepo(){
  printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"
  hugo -t jane # if using a theme, replace with `hugo -t <YOURTHEME>`

  cd public && git add .
  msg="the new archive updating. $(date)"
  git commit -m "$msg" && git push
  echo "\n" 
  printf "\033[0;32msee it  https://66418500.github.io/ \033[0m\n"
}


geneNewArchives
pushTorepo
