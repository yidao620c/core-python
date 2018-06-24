
打包GUI程序步骤

## 安装PyInstaller

```
pip install PyInstaller
```

## 打包图片资源文件

```
pyi-makespec options love.py
```

来生成一个spec文件，再来就是增加我们需要的资源文件。

```
a.datas += [('1.gif', 'D:\\projects\\xncoding\gui\\core-python\\mygui\\1.gif')]
```

## 打包成exe文件

```
pyinstaller -F love.py --noconsole
```

然后再dist目录就能找到这个exe文件，双击可运行了
