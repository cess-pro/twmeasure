# twmeasure
tsinghua 计算机网络管理课程作业

json是最终形成的文件，用来存储所有主机的信息

# TODO:
- [ ] 搜集TW地区GOV具体的IP地址目标

    - [x] 通过gov.tw ，同时更新主机关联域名

    - [x] 通过获取NX记录获取，同时更新主机关联域名

    - [x] 通过GSV网络号获取，AS4782 

- [ ] 探测主机存活 

- [ ] 获取主机地理位置 

- [ ] 获取主机traceroute信息 

- [ ] 获取主机开放端口信息 

# working
# x:

搜集gov.tw子域名，并获取A记录NX记录

    通过Sublist3r程序获取了gov.tw的所有公开情报子域名
    
    已经通过DNS查询对所有公开的网址信息进行了地址确认，并更新了targets.json
