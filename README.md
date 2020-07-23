# HTML Tag Summarizer
- HTMLタグの要約作成
- お遊び
## env
- pyenv
- venv
  - pip install -r requirements.txt
## procedure 
- python htmltagsummarizer.py
- python segmentation.py
- python summarizer.py
## result
- 微妙
```
{
  "a": [
    "例えばまだリンク先がまだ存在しないあるいは存在したが削除された場合などhref属性を持たないa要素を配置することでダミーリンクとすることができます",
    "対象となる要素にid属性を使用して名前を付けておきa要素のhref属性値に名前という形式で指定することでその場所に移動することができます",
    "a要素のコンテンツモデルはトランスペアレントコンテンツです",
    "例えばa要素がフローコンテンツをコンテンツモデルに持つ要素内の子要素として使われる場合そのコンテンツモデルもフローコンテンツとなります",
    "これによってa要素はHTMLなどでは許されていなかったp要素やdiv要素section要素などを内包することが可能になりました"
  ],
  "abbr": [
    "abbr要素は略称や頭字語を表します",
    "例えばWCという略称に対してabbr要素でマークアップすることでそれが略称だということを意味づけします",
    "またtitle属性をあわせて使うことで略称の正式名称を指定することもできます",
    "title属性を使用する場合は略称の正式名称以外を値として記述してはいけません",
    "title属性値は多くのブラウザでツールチップとして利用されています"
  ],
  "address": [
    "直近の先祖となる要素がbody要素の場合address要素でマークアップされた連絡先情報は文書全体に対する連絡先情報となります",
    "複数の著者で運営されるWebサイトなどでは使い分けることでWebサイト全体に対する連絡先と個別の記事に対する連絡先を明示することが可能です",
    "におけるaddress要素は明確にその文書あるいは記事の連絡先となる情報のみをマークアップするための要素となります",
    "また文書や記事の中でその文書や記事の連絡先とは関係のない住所電話番号メールアドレスなどが出てくる場合にもこれらをaddress要素でマークアップすることは適切ではありません",
    "ただしヘッディングコンテンツhhセクショニングコンテンツsection要素やaside要素header要素footer要素address要素を含むことはできません"
  ],
```
