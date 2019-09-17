# Switch 游戏销售折扣爬虫

> Switch 平台游戏各个地区折扣价格

Jump小程序和Savecoins网站的游戏折扣信息

## 爬虫介绍
* jump
* savecoins

## 目录

[环境安装](#环境安装)

[快速启动](#快速启动)

## 安装
1. 下载安装Python3.5或以上版本
2. 安装Mysql数据库并执行[game.sql](game.sql)脚本初始化数据库表.
3. 在`DG/`目录下[pipelines.py](DG/pipelines.py)文件中修改数据库链接信息.
```python

    config = {
        'user': 'xx',  //用户名
        'password': 'xxx', //密码
        'host': 'xx.xx.xx.xx', //ip
        'database': 'xx', //数据库
        'charset':'utf8mb4'
    }

```
3. 安装依赖,在项目根目录执行
```bash
pip install -r requirements.txt
```

## 使用

执行 `run.sh`,启动爬虫.

```bash
chmod +x ./run.sh && ./run.sh
``` 

## Maintainers
[@yangb92](https://github.com/yangb92)

## License
© 2020 杨斌