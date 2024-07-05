# 第３章　配布パッケージの配布方法とインストール動作方法

## 事前準備

本サンプルコードをWindowsで実施する場合は、そのコマンドラインの開始時に次のコマンドを実行し、一時的にPython.exeへパスを通してから開始してください。

```
set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python311
```



## 3.2節　パッケージの動作確認（作成手段に依存せず同一）

本節で案内のコマンド例を以下へ記載します。
こちらはLinux環境での例のため、Windows環境では「`source .venv/bin/activate`」を「`.venv\Scripts\activate`」に変更してください。

```
python -m venv .venv
source .venv/bin/activate

python -m weatherforecast
pip install [whlファイルの格納フォルダーへのパス]/weatherforecast-0.0.1-py3-none-any.whl

python -m weatherforecast

deactivate

python -m venv --clear .venv
```

