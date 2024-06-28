# 第２章　配布パッケージの作成手順


## 各節に共通する事前準備

本サンプルコードをWindowsで実施する場合は、そのコマンドラインの開始時に次のコマンドを実行し、一時的にPython.exeへパスを通してから開始してください。

```
set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python311
```



## 2.2節と2.3節に共通する事前準備

初回実行時には、対象フォルダー直下でコマンドラインから次のコマンドを実行して仮想環境を作成してください。

```
python -m venv .venv 
```

2回目以降は、次のコマンドで作成済みの仮想環境に入ってください。


Windowsの場合：
```
.venv\Scripts\activate
```

Linuxの場合：
```
source .venv/bin/activate
```



## 2.2節　解説に用いるサンプルパッケージの構成

[section2-2](./section2-2)



## 2.3節　作成時の依存関係の管理にpipを用いるケース

[section2-3-3, Setup() 関数による配布パッケージの作成](./section2-3-3)

[section2-3-4, buildコマンドによる配布パッケージの作成](./section2-3-4)



## 2.4節　作成時の依存関係の管理にpoetryを用いるケース

[section2-4](./section2-4)


