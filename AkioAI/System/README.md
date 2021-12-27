#AkioAI

## 1.アプリ概要

AkioAI は、web スクレイピングと重回帰分析を使用した競馬予想をするシステムです。予想した結果を Instagram で発信しています。

## 2.使用技術

- 使用言語

  - Python 3.8.5

- 主要ライブラリ
  - Pandas
  - Beautiful Soup
  - Scikit-learn

## 3.アプリの特徴

- 情報が必要最低限である  
   　一目で分かるようなデザイン構造になっていて、直感的に馬を選ぶことができます。初めて出馬表を見たときに、情報量が多すぎて困惑する人は少なくないかと思います。見たことない方も、どこを見たら良いか分からないはずです。
  　しかし AkioAI の表示項目は、馬番、馬名、騎手、指数（全体評価値）の 4 つだけです。初心者が困惑しがちな専門的用語は使用していないので、初心者にとってハードルが低く、予想がしやすい仕様になっています。  
   ![result](https://user-images.githubusercontent.com/91531795/147451512-527e4ecd-f569-4ccd-9ace-6cb33e18ae75.jpg)

## 4.アプリ構造

1.  main.py(class_main.py)  
    [netkeiba.com](https://www.netkeiba.com/?rf=navi)から過去のレースデータを、web スクレイピングします。
2.  processing.py(class_processing.py), kaiki.py(class_exp.py)  
    スクレイピングしたデータを標準化し、重回帰分析を行います。
3.  demo.py(class_demo.py)  
    分析結果を基に、デモンストレーションを実施します。
4.  output.py(class_output.py)  
    実際に行われるレースの予想を行います。
