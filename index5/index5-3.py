# coding:utf8
# 如何设置文件的缓冲

'''
实际案例:
将文件内容写入到硬件设备时,使用系统调用,这类I/O操纵的时间很长
为了减少I/O操作的次数,文件通常使用缓冲区(有足够的数据才进行系统调用)
文件的缓冲行为,分为全缓冲,行缓冲,无缓冲

如何设置python中文件对象的缓冲行为
'''
'''
解决方案:
全缓冲: open函数的buffering设置为大于1的整数n,n为缓冲区大小
       缓存区满了就将buffering大小的字符写入到
行缓冲: open函数的buffering设置为1 按行写入到文件,
       检查到换行就上一行之前的字符写入到文件
无缓冲: open函数的buffering设置为0 实时写入
'''

# 如何将文件映射到内存
'''
实际案例:
1.在访问某些二进制文件时,希望能
把文件映射到内存中,可以实现随机访问(framebuffer设备文件)
2.某些嵌入式设备,寄存器被编址到内存地址空间,我们可以映射/dev
/mem某范围,去访问这些寄存器
3.如果多个进程映射同一个文件,还能实现进程通信的目的

解决方案:
使用标准库中mmap模块的mmap()函数,他需要一个打开的文件
描述符作为参数
'''

# 如何访问文件的状态
'''
实际案例:在某些项目中,我们需要获得文件状态,例如:
1.文件的类型(file,directory,符号链接,设备文件)
f = open('demo.wav')
d = f.fileno()
s = os.fstat(d)
huozhe
s = os.stat('file access')
huozhe
os.path.isfile('demo.wav')
stat.S_ISREG(s.st_mode)
2.文件的访问权限,判断是否为TRUE
s.st_mode & stat.S_IXUSR
s.st_mode & stat.S_IRUSR
s.st_mode & stat.S_IWUSR

3.文件的最后的访问/修改/节点状态更改时间
st_atime,st_mtime,st_ctime
os.path.getatime('demo.wav')
4.普通文件的大小
os.path.getsize('demo.wav')
'''
'''
解决方案:
系统调用:标准库中os模块下的三个系统调用stat,
fstat,lstat获取文件状态
快捷函数:标准库中os.path下一些函数,使用起来更加简洁



Out[88]: posix.stat_result(st_mode=33279, st_ino=1572995, st_dev=43, st_nlink=1, st_uid=1000, st_gid=1000, st_size=31227548, st_atime=1526651936, st_mtime=1465568279, st_ctime=1526651936)

Out[89]: posix.stat_result(st_mode=33279, st_ino=1572995, st_dev=43, st_nlink=1, st_uid=1000, st_gid=1000, st_size=31227548, st_atime=1526651936, st_mtime=1465568279, st_ctime=1526651936)
Out[94]: posix.stat_result(st_mode=33279, st_ino=1572995, st_dev=43, st_nlink=1, st_uid=1000, st_gid=1000, st_size=31227548, st_atime=1526651936, st_mtime=1465568279, st_ctime=1526651936)

'''




