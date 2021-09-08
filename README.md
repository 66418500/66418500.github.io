# hugoblog-
# 1.Environmental installation
* hugo
* https://gohugo.io/getting-started/installing/
* fortune
```
#centos
yum install fortune-mod

#ubuntu
sudo apt-get install -y fortune
```

# 2.The deployment scripts
**pushMyblog.sh** 
* This script has two functions, one for generating static files. One for pushing to the remote repo. A .github/workflows/public.yml file used to deploy an automated build.

* see it https://github.com/66418500/66418500.github.io/blob/blog/pushMyblog.sh
* visit the hugo page https://66418500.github.io/ 

**pushMyblog.py**
