# 第2章　配布パッケージの作成手順

最初に、「[各節に共通する事前準備](../README.md#各節に共通する事前準備)」と「[2.2節と2.3節に共通する事前準備](#22節と23節に共通する事前準備)」を実施してください。



## 2.2節：解説に用いるサンプルパッケージの構成

「リスト2.2：サンプルコードのパッケージ構成」のサンプルコードです。

依存関係のパッケージは含んでおりませんので、初回はコマンドラインから本フォルダー上にて次のコマンドを実行してください（必要パッケージがインストールされます）。

```
python -m pip install   requests numpy
```

本サンプルの動作確認を行うに、次のコマンドを実行します。

```
python -m weatherforecast
```


上述の操作の詳細は、続く節の「§2.3.1：仮想環境venvの作成」と「§2.3.2：仮想環境に依存関係をインストールし、サンプルの動作確認」に記載していますので、参照ください。

参考までに、初回の仮想環境作成を含めた全体の実行コマンドを以下へ記載します。

Windowsの場合：
```
python -m venv .venv
.venv\Scripts\activate
pip list
python -m pip install   requests numpy
python -m weatherforecast
deactivate
```

Linuxの場合：
```
python -m venv .venv
source .venv/bin/activate
pip list
python -m pip install   requests numpy
python -m weatherforecast
deactivate
```



### 本サンプルコードの動作仕様

次の3つの機能（関数）を提供します。

* 指定された地点の向こう2週間の1時間おきの予想気温の配列と対応する時刻の配列を、要素に持つ辞書オブジェクト（dictionary object）を返却
    * `def get(location: str = "tokyo") -> dict:`
    * 引数には地点の指定を文字列で設定。有効な値は以下。
      * `tokyo`, `nagoya`, `osaka`
    * 返却値の辞書オブジェクトが有するキーは以下
      * `location`　　　：指定した地点の文字列
      * `time`　　　　　：時刻の配列
      * `temperature_2m`：1時間おきの予想気温の配列      
<!-- 有効な文字列を返却する関数を定義するべき -->

* 渡された予想気温の配列に対して、最大値、平均値、最小値を辞書オブジェクト（dictionary objecct）を返却
    * `def apply(temperature_list: list) -> dict:`
    * 返却値の辞書オブジェクトが有するキーは以下
        * `mean`：平均値
        * `max` ：最大値
        * `min` ：最小値

* 東京の向こう2週間の1時間おきの予想気温の配列と対応する時刻の配列を、コンソールにprint()文で出力する
  * `def main() -> None:`
  * コンソールからの動作確認用
  * 実体としては、`get("tokyo")`と等しい
  * 実行結果例は以下

```
tokyo
['2023-10-23T00:00', '2023-10-23T01:00', ..., '2023-10-29T23:00']
[13.2, 12.9, ... , 14.4]
```


