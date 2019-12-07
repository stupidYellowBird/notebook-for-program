# os模块
import os

# 系统的路径分割符
os.sep 
# 操作系统的平台，window 对应于nt，linux/unix 对应于posix
os.name
# 获取操作系统的换行符,window->'\r\n',linux/unix ->'\n',mac ->'\r'
os.linesep
# 获取当前工作目录，即主脚本的工作目录
os.getcwd() 
# 获取指定目录的文件和目录名
os.listdir(path)
# 改变当前目录，如果允许访问返回 True ,否则返回 False
os.chdir(path)

# 创建目录，mode为权限数字模式，默认为0777，4+2+1=7 
os.mkdir(path,mode)

os.makedirs(name)
# 方法用于创建一个管道, 返回一对文件描述符(r, w) 分别为读和写
# os.pipe()  ->(r,w)
# 删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError
os.remove(path)
os.removedirs(name)
# 改变文件名
os.rename(src,dst)

# 删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
os.rmdir(path)
os.replace(src,dst)
os.scandir(path)
os.sendfile()
os.stat(path)
os.chmod(path,mode)
os.chown(path,uid,gid)

# 检测当前的uid和gid对path是否有访问权限，mode为
# os.W_OK(可写) os.R_OK(可读) os.X_OK(可执行) os.F_OK(文件是否存在) 
os.access(path,mode)

os.chroot(path)
os.cpu_count()
# 复制一个文件描述符
os.dup(fd)
# 将一个文件描述符 fd 复制到另一个 fd2
os.dup2(fd,fd2)
# 创建一个硬链接
os.link(src, dst)
# 创建一个软链接
os.symlink(src, dst) 

os.system(command)
# 路劲树生成器
os.walk(top,topdown)

# 获取环境变量
os.getenv(key:text,default)
# 设置环境变量
os.putenv(key,value)

