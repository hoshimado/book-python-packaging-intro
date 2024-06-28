# 第2章　配布パッケージの作成手順

最初に、[各節に共通する事前準備](../README.md#各節に共通する事前準備)を実施してください。



## 2.4節：作成時の依存関係の管理にpoetryを用いるケース

本節の初回実行時には、紙面の記載のコラム「poetryのインストール方法」にしたがってpoetryコマンドをインストールしてください。
poetryインストールに用いるコマンドは次の通りです。

推奨されるpoetryインストールコマンド:
```
# Linux, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Windows (Powershell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

プロジェクトごとに仮想環境を作成するように設定：
```
poetry config virtualenvs.in-project true
```



### 2.4.2節：仮想環境poetry shellを作成

「2.4.1節：プロジェクトを作成」を含めて、次の手順を終えた状態の
「リスト2.24：poetryによる配布パッケージ作成用のフォルダー構成例」のサンプルコードです。

1. 「2.4.1節：プロジェクトを作成」を実施
2. 「リスト2.19：Poetryによる仮想環境を作成する」を実施
3. 「リスト2.23：poetryの仮想環境に依存関係のパッケージを追加する」を実施
4. パッケージのフォルダーであるweatherforecastへサンプルコードの配置（置き換え）

お手元での上述の手順の実施後の、完成状態の比較としてお使いください。
手順を実施する際の「パッケージのフォルダーであるweatherforecastをサンプルコードのフォルダーで置き換えます」の置き換え元のサンプルコードは、
「2.2節：解説に用いるサンプルパッケージの構成」で提示のフォルダー「[weatherforecast](../section2-2/weatherforecast)」を用いてください。

なお、上述の手順をスキップし、本フォルダーの内容を直接に利用する場合は、本フォルダーの内容を任意のフォルダーに格納後、次のコマンドを実行してください。「リスト2.19」や「リスト2.23」の操作を実行済みの状態を再現できます。

```
poetry install
```



### 2.4.3節：poetryコマンドによる配布パッケージの作成

本節で案内のコマンドを以下へ記載します。

```
poetry build
```



