#WebSSHAgent

##利用shellinabox

shellinabox有一个启动参数-s可以指定打开什么服务，并且在该启动参数可以传递参数，通过在最终执行的工具前输入格式为key=value的字段即可，以空格为分割，可以传递多个字段，并且支持扩展变量，例如：

- ${columns} number of columns.
- ${gid} numeric group id.
- ${group} group name.
- ${home} home directory.
- ${lines} number of rows.
- ${peer} name of remote peer.
- ${uid} numeric user id.
- ${url} the URL that serves the terminal session.
- ${user} user name.


其中${url}可以传递url，所以：

当我们这么启动shellinbox后：

	shellinaboxd -t -s '/dcloud:root:root:/:b=${home} url=${url} /bin/bash' 

就可以在shell中通过$url获取到当前的url，效果如下：

![](http://images2015.cnblogs.com/blog/756310/201702/756310-20170220203707710-542480378.png)


可以看到url已经传递到shell中，所以我们可以通过指定url的方式来指定要access的容器信息，例如容器的IP和容器名等。

###参考文献

[shellinabox官方manual](https://github.com/shellinabox/shellinabox/wiki/Shell-In-A-Box-manual)

##在宿主机上设置一个agent

光有shellinabox只能访问到宿主机，我们的目的是直接操作容器，利用docker exec命令可以直接在宿主机上对docker容器执行命令，所以我们需要对web端的shell传过来的命令做一个处理和转发。比如用户想对名为'ubuntu'的容器执行'ls'命令，那么我们实际执行的命令应该是:

	docker exec ubuntu ls

并且把结果返回。

这里我的思路是利用python的os包下的popen方法，该方法可以执行系统命令并且返回结果。


## 启动shellinabox

	shellinaboxd -t -s '/dcloud:root:root:/:b=${home} url=${url} /root/shell/WebsshAgent/dist/shell/shell' --css=/usr/share/shellinabox/white-on-black.css -b
