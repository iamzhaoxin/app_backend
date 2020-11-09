# :point_right:大创APP后端开发  

![language-python](https://img.shields.io/badge/language-python_3.8.0-brightgreen.svg?style=plastic)  ![大佬-通哥哥](https://img.shields.io/badge/大佬-通哥哥-brightgreen.svg?style=plastic)  
## 学习目标
[实现前端功能设计](/api_design.md)  
[数据库设计](/mysql_design.md)  
[大事记](/Memorabilia.md)(每周总结)

## 学习内容
+ `GitHub`&`git`的使用
+ *Python*后端开发
+ 前后端交互

## 新设备部署
1. git clone

2. git config --global http.https://github.com.proxy socks5://127.0.0.1:7890

3. 修改文件`/venv/pyvenv.cfg`，内容为
    ```
    home = D:\tools\Python38	#改为当前python安装路径(这个注释要删掉！)
    include-system-site-packages = false
    version = 3.8.0
    ```
4. 文件-设置-项目-Python解释器-选择venv文件夹里Scripts文件夹里的python.exe文件

5. 右上角添加Django服务器配置



## 开发流程
1. 本地dev分支修改代码
2. push到远程dev分支  
……
3. 完成阶段功能后，本地将dev合并到master，并push到远程master，本地切换回dev

———————————————————————————————————————————————   
***欢迎issue***