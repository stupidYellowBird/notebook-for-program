
### 安装后需要一些配置
git config --global user.name ""
git config --global user.email ""
git config --list 可查看当前用户信息以及其他的一些信息

### 建立本地git仓库
git init

### 将项目的所有文件添加到缓存中:git add . 
 
git add . (注意,后面有个点)表示添加目录下所有文件到缓存库,如果只添加某个文件,只需把 . 换成你要添加的文件名即可;


### 将缓存中的文件Commit到git库

git commit -m "添加你的注释,一般是一些更改信息"

### 建立远程库

### 将本地的库链接到远

终端中输入: git remote add origin HTTPS链接

### 上传代码到远程库,上传之前最好先Pull一下,再执行命令: git pull origin master

### 接着执行:git push origin master