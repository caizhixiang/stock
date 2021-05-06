# stock
python 股票分析
----scrapy爬虫框架
1. 环境安装
   -mac | linux:  pip install scrapy
   -win10  :
            - pip install wheel
            - 下载twisted,下载地址为：https://www.lfd.uci.edu/~gohlke/pythonlibs/
            - 安装twisted, pip install Twisted-20.3.0-cp38-cp38-win_amd64.whl
            - pip install pywin32
            - pip isntall scrapy
        测试：在终端输入scrapy指令，没有报错即成功。
2. 使用
    - 创建工程：scrapy startproject xxxPro
    - cd xxxPro
    - 在spiders子目录里创建一个爬虫文件
      - scrapy genspider spiderName www.xxx.com
    - 执行工程：
      - scrapy crawl spiderName
    
3. 五大核心组件
    - 数据解析 
        - spiders/first.py
            - name  爬虫名称
            - start_urls    解析的初始urls
            - parse（）   response.xpath().extract()
    - settings.py  配置文件
    - 管道数据持久化
        - 编码流程
            - 数据解析
            - 在item类中定义相关的属性
            - 将解析的数据封装存储到item类型的对象
            - 将item类型的对象提交到管道进行持久化
            - 在管道里pipelines.py 中process_item（）方法中进行持久化
            - 在配置文件中开启管道
    - 中间件
        - 下载中间件
            - 位置：引擎和下载器之间
            - 作用：批量拦截到整个工程中所有的请求和相应
            - 拦截请求：
                - UA伪装：process_request（）
                - 代理IP:process_exception（）:return  request
            - 拦截相应：
                - 篡改响应数据，响应对象（动态加载页面）:process_response（）方法里用selenium动态加载js
                    - 安装selenium及浏览器驱动：pip install selenium  &&下载驱动 http://npm.taobao.org/mirrors/chromedriver/