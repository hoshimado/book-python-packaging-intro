import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="open-meteo-weather-sample-jpcity", # PEP503, PEP508に従いハイフンのフォーマットでパッケージ名を設定
    version="0.0.1",           # PEP 440で指定された公式のバージョン表記で設定
    # python_requires='>=3.7', # Pythonバージョンに縛りがある場合は設定
    install_requires = requirements, # 依存関係を requirements.txt から読み込んで設定（情報としては同一）
    entry_points={
        'console_scripts': [
            'open_meteo_weather_sample_jpcity=open_meteo_weather_sample_jpcity:main',
            # PEP8に従いアンダースコア
        ],
    },
    packages=setuptools.find_packages(), # 直下のパッケージのフォルダ名をリスト形式で全て取得
    description="sample distribution-packages by legacy-setup.py", # パッケージの簡単な説明を記載
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT License",
    author="Madokawa Hoshiki"
)
