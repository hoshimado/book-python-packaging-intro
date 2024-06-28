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



## D：配布パッケージ化をGitHub Actionsで自動化する（CI 構築）


