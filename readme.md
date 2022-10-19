## 简介

通过扫描naifu默认6969端口得到正在运行naifu的主机地址。

推荐在大型局域网如校园网下扫描局域网段，扫描公网段效率极低。

A类地址：10.0.0.0 - 10.255.255.255

B类地址：172.16.0.0 - 172.31.255.255

C类地址：192.168.0.0 - 192.168.255.255



## 使用说明

###安装依赖

```
pip install -r requirements.txt
```

###扫描ip段

例如扫描需要10.0.0.0到10.2.255.255的所有6969端口，一轮扫描停止后3600秒开始下一轮扫描。

```
python main.py --f '10.0.0.0' --t '10.2.255.255' --i 3600
```

扫描结果记录在open_port.txt文件中，可重复扫描添加上一轮没扫描到的地址。

建议查看自己在局域网中的ip地址，酌情扫描相邻的ip段。

###检测在线服务

检测open_port.txt中记录的地址的当前在线数。

```
python online_test.py
```

###批量提交任务

```
python post.py --pmpt 'example' --uc 'example'
```

从open_port.txt中自动向在线的地址一次提交生成一张图片的任务，得到返回图片后再次循环提交，无限循环提交任务，需要手动终止，生成的图片保存在images文件夹中。

####参数说明

| args | description | type | default |
| ---- | ----- | -----  |----- |
| --pmpt | 正面标签 | str | None |
| --uc  | 负面标签 | str | None |
| --w  | 宽度 | int | 512 |
| --h  | 高度 | int | 768 |
| --stp  | 步数 | int | 28 |
| --scl  | 服从度 | int | 12 |

**可持续式发展，切勿滥用！**