# 付録

## 付録B：本書で利用するPython環境のインストール方法

本節で案内のコマンドとサンプルコードは、以下を参照ください。

* リストB.1：対象のコマンドライン内でのみ有効なPATHを追加設定する
    ```
    set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python311
    ```
    ※「リストB.1」のコマンドは、[第２章の各節に共通する事前準備](../chapter02/README.md#各節に共通する事前準備)と同一です。

* リストB.2：Python環境作成用のDockerfile
    * [Dockerfile](../docker/Dockerfile)



## 付録C：パッケージ化の前にソース難読化を実施する（Pyarmor）

> **改行コードに関する注意：**
>
> 取得したシェルスクリプトを実行する際に、次のようなエラーとなることがあります。
> > : not found_XXX.sh: line 1: #!/bin/bash
> 
> これは、Windows環境などでGitリポジトリから取得した際に、設定によっては改行コードがCFからCRCFへ自動変換されてしまうことに依ります。
> 任意のエディターを用いて改行コードをCFに戻したうえで再実行してください。
>

[C.2：Setup()関数による配布パッケージの作成手順](./c2-obfuscate-setuppy/)

[C.3：poetryコマンドによる配布パッケージの作成手順](./c3-obfuscate-poetry/)



## 付録D：配布パッケージ化をGitHub Actionsで自動化する（CI 構築）

本節で案内のワークフローファイルは、以下を参照ください。

* [リストD.1：setup.pyを用いた配布パッケージの作成のワークフロー](../.github/workflows/python-package-legacy.yml)
    * [section2-3-3](../chapter02/section2-3-3/)に格納してあるファイルに対して実施
* [リストD.2：poetryを用いた配布パッケージの作成のワークフロー](../.github/workflows/python-package-poetry.yml)
    * [section2-4](../chapter02/section2-4/)に格納してあるファイルに対して実施
* [リストD.3：poetryを用いた配布パッケージの作成を、難読化込みで実施するワークフロー](../.github/workflows/python-package-poetry-with-pyarmor.yml)
    * [C.3：poetryコマンドによる配布パッケージの作成手順](./c3-obfuscate-poetry/)に格納してあるファイルに対して実施

いずれのワークフローも、変数「`TARGET_DIR`」を用いて対象のサブフォルダー内のパッケージ構成ファイルに対して配布パッケージ作成を行う構成としています。対象のパッケージをルートフォルダーに置いている場合は「`TARGET_DIR: .`」のように修正してください。

なお、それぞれのワークフローにより自動作成された配布パッケージの具体例を、本リポジトリーの「[Actionsタブ](https://github.com/hoshimado/book-python-packaging-intro/actions)」から参照できます。




## 付録E：Python配布パッケージをGitHubリポジトリで配布する方法

「リストE.1：Publicリポジトリからpipコマンドでインストールする」を、
本リポジトリ（Public設定）のルートに配置してある「[pyproject.toml](../pyproject.toml)」に対して
適用すると、具体的なコマンドは以下となります。

```
python -m pip install git+https://github.com/hoshimado/book-python-packaging-intro.git
```



## 付録F：Python配布パッケージをPyPIリポジトリで配布する方法

F.1節「配布パッケージを、PyPI公開用に整える」に記載の手順を実施した結果のサンプルコードは、以下を参照ください。

* [setup()関数による配布パッケージ、の場合](./f1-distribute-from-pypi/setuppy-style/)
    * 以下の変更を反映済みのものとなります
        * リストF.5
        * リストF.7
        * リストF.9
* [buildコマンドによる配布パッケージ、の場合](./f1-distribute-from-pypi/pytoml-style/)
    * 以下の変更を反映済みのものとなります
        * リストF.6
        * リストF.8
        * リストF.10

F.4節「配布パッケージをアップロードする」にしたがってPyPIへアップロードしたものは以下で参照できます（※実際のアップロードファイルでは、README.mdへの更新履歴などに差分があります）。

* https://pypi.org/project/open-meteo-weather-sample-jpcity/



## 付録G：





