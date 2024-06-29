# 付録C：パッケージ化の前にソース難読化を実施する（Pyarmor）

## C.2：Setup()関数による配布パッケージの作成手順

本節で案内の手順を終えたサンプルコードです。
「リストC.2：Pyarmorで難読化したのちにsetup.pyで配布パッケージを作成する」のファイルは、
「[build_whl_with_pyarmor.sh](./build_whl_with_pyarmor.sh)」を参照ください。

シェルスクリプトとして作成しているので、「付録B：本書で利用するPython環境のインストール方法」で案内しているLinuxのDocker環境で実行するか、同様のLinux環境で実行してください。

「build_whl_with_pyarmor.sh」を実行後、`./dist` フォルダー配下に `weatherforecast-0.0.1-py3-none-any.whl` が作成されます。このWheelファイルを展開して、パッケージ内のソースコード（例えば`open_meteo_forecast_api.py`）が難読化されていることを確認ください。

この難読化を実施したWheelファイルを、インストールして利用する分には通常の配布パッケージと同様に利用できることを確認するコマンド例は以下です。第3章で案内した「[パッケージの動作確認](../../chapter03/README.md)」に沿い、Wheelファイルをインストール前はパッケージを実行できないことを確認した後に、Wheelファイルをインストールするとパッケージを実行できることを確認する手順となります。

```
cd ./dist
python -m venv .venv-wsl39 
source .venv-wsl39/bin/activate

python -m weatherforecast
    No module named weatherforecast

python -m pip install weatherforecast-0.0.1-py3-none-any.whl
python -m weatherforecast
    （パッケージの実行結果が出力される）
    
deactivate
```



### 本サンプルコードに含まれるファイルの補足

* 「2.3.3節」の[setup.py](../../chapter02/section2-3-3/setup.py) に対して、本節の手順を実施した変更後のファイルは、[setup.py](./setup.py)となります


