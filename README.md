## vscode設定
基本的にvscode推奨。他のエディタを利用する場合は、自己責任です。
### .vscode/extensions.json
本プロジェクトで必要なvscodeプラグインが記載されています(プロジェクトを開くと自動的にインストール指示が出ます)

### .vscode/settings.json
本プロジェクトで必要なlinterやformatterの設定がされています。これは各自で追記、または別の設定が入っている場合はコメントアウトしてください。
## Python設定
[ここ](https://github.com/shuntaka9576/python_project_sample#%E5%8F%82%E8%80%83%E8%B3%87%E6%96%99)の記事をみて、作りました。
### Pythonバージョン
version 3.7.4
### Linter(3つ)
#### mypy
型チェックをしてくれるlinter
#### flake8
PyFlakes, pycodestyle, mccabeのラッパー。pep8準拠とか、論理的エラー、循環複雑度をチェックしてくれる
### formatter
#### isort
import部分を綺麗にしてくれる(Ctl+cmd+pで)
vscodeだと、Command Palette (⇧⌘P), then Python Refactor: Sort Importsで実行可能
* [ ] 自動的にやりたい
#### black
フォーマッター。記法を強制的に統一してくれる(autopep8よりこっちのが流行ってそう)
### 型定義
引数と戻り値には、型定義をする(Python3.5の機能)
```python
def greeting(name: str) -> str:
    return "Hello " + name


if __name__ == "__main__":
    greeting(1)
    # =>Argument 1 to "greeting" has incompatible type "int"; expected "str"mypy(error)
    greeting("world")
```

### Test tool
#### pytest
#### tox
なんか便利らしー。調べたい。

## プロジェクトの動かし方
### 環境変数の設定
.bash_profileとか.zshprofileとかに以下を追記
```bash
export PIPENV_VENV_IN_PROJECT=true
```
### 依存ライブラリのインストール
```bash
pipenv install --dev
```

## その他
### .gitignore
[githubのデフォルトテンプレートを使用](https://github.com/github/gitignore/blob/master/Python.gitignore)
### やりたいなぁと思っていること
* pre-commitでlinter, formatter実行、落ちたらコミット出来ない設定

## 環境の初期構築(ここはやらなくて良い)
このリポジトリを作るときに使ったコマンドのメモです
```
pipenv install --python 3.7
curl -L https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -o .gitignore
```

## 参考資料
### プロジェクト構成周り
aodag先生素晴らしい
* [Python 3.7とVisual Studio Codeで型チェックが捗る内作Pythonアプリケーション開発環境の構築](https://qiita.com/shibukawa/items/1650724daf117fad6ccd)
* [Pythonでの開発を効率的に進めるためのツール設定](https://www.slideshare.net/aodag/python-172432039)
### 型周り
* [Pythonではじまる、型のある世界](https://qiita.com/icoxfog417/items/c17eb042f4735b7924a3)
* [Pythonで型検査しようぜ](http://kk-river108.hatenablog.com/entry/2019/03/10/163457)
