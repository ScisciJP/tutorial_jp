# ScisciJP 2024 Tutorial

Scisci分野の論文およびコードのチュートリアル。
2024年の3/17開催のScience of Science研究会の前日イベントとして開催。

SciSciとはどのような分野なのか、どのような問いのもとにどのようなデータを扱って分析を行なっているのか、
加えてそれらの手法や指標の利点と限界について、概要を学びます。

# Getting Started

以下4つの章を手元ですぐに試しながら学習を進められるよう、google colaboratoryというサービスで環境を構築してあります。
これら4つの章は [#Table of Contents](https://github.com/ScisciJP/scisciJP2024_tutorial#table-of-contents) の4つの章にそれぞれ順に対応しています。

[ハンズオン](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/1-GettingStarted.ipynb) -> [Scisci分析の実例を見てみる](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/2_CitationClustering.ipynb)　-> [論文を自分で再現してみる](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/3-Disruptiveness.ipynb) -> [演習：OpenAlexやその他のデータベースを自分で触れるようにする](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/4-H-index.ipynb)

それぞれの章は概ね独立していますので、好きな章から試してください。


# Table of Contents
- [Getting Started](./1-GettingStarted.ipynb) 
     - Science of science でどのようなデータを取り扱うのか、”Open Alex”というサービスを使っていくつか分析する中で確認しましょう。
- [Visualizing Science](./2_CitationClustering.ipynb)
     - 引用関係を使って論文のネットワークを作り、論文が密に疎に繋がっている様子から分野を抽出できるか検証してみましょう。
- [Research Evaluation](./3-Disruptiveness.ipynb)
     - 研究者評価の指標として、科学におけるインパクトを定量化する手法の一つとして現在ホットな"Disruption Index”を学びます。対象論文の引用ネットワークにおける親と子を含めた3世代間の引用比で論文の革新性を表現した論文を再現してみましょう。
- [Researcher Evaluation](./4-H-index.ipynb)
     - 研究者の評価指標として、"h-index"を算出し、さらに個々の研究者のh-indexを他の変数から推定してみます。様々な交絡を考慮してより精度高く推定してみてください。

