## 安装运行
```
pip install Flask

cd utou
python -m flask run --host=0.0.0.0 --port=80
```

## uWSGI 运行
https://dormousehole.readthedocs.io/en/latest/deploying/uwsgi.html

## 接口
```
 /
 /del?sign=密钥key&url=完整域名
 /add?sign=密钥key&url=完整域名
 /showall?sign=密钥key
```