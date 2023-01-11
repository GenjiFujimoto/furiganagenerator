
This is a program to generate furigana, given japanese input. It is based on a machine learning approach and was trained with a couple of ジュニア文庫 books. However input data wasn't always perfect and as these books were meant for a younger audience, this also probably won't recognize more obscure kanji or complicated expressions.
However testing on a small sample already resulted in ~98.5% accuracy.

## Usage
```
$ python ./addfurigana2.py "見飽きた三つの雁首に向かって、スバルは地面を踏み鳴らして怒りをぶつける。三度の邂逅"
> 見[み]飽[あ]きた三[みっ]つの雁[がん]首[くび]に向[む]かって、スバルは地[じ]面[めん]を踏[ふ]み鳴[な]らして怒[いか]りをぶつける。三[さん]度[ど]の邂[かい]逅[こう]
```
