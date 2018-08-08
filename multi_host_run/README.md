# multi_host_run.py

基于[fabric](http://www.fabfile.org/)兼容`fabric1.x`和`fabric2.x`，用于多主机上执行命令。

## 如何运行

### 增加可执行权限

```
$ cd multi_host_run
$ chmod +x multi_host_run.py
```

### 添加到环境变量中

```$ export PATH=/your/path/for/multi_host_run:$PATH```

### 配置主机和日志目录

修改`base.py`中`LOG_PATH`和`HOSTS`，注意**必须使用SSH密钥验证登陆**。

### 运行

#### 使用-c指定执行命令

```$ multi_host_run.py -c command```

#### 选项-l和-p是定制的，用于进入日志目录并搜索登陆日志和支付日志

```
$ multi_host_run.py -l openId
$ multi_host_run.py -p queryId
```

### 参看帮助

```$ multi_host_run.py -h```

