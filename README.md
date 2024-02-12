# ScisciJP 2024 Tutorial

Scisci分野の論文およびコードのチュートリアル。
2024年の3/17開催のScience of Science研究会の前日イベントとして開催。

SciSciとはどのような分野なのか、どのような問いのもとにどのようなデータを扱って分析を行なっているのか、
加えてそれらの手法や指標の利点と限界について、概要を学びます。

本チュートリアルは、

[ハンズオン](./GettingStarted.ipynb)→[初級の分析](./CitationClustering.ipynb)→[中級の分析](./Disruptiveness.ipynb)（論文の再現）→[演習](./H-index.ipynb)

の順に構成しています。

# Table of Contents
- [Getting Started](./1-GettingStarted.ipynb) - ”Open Alex”というサービスを使ってSciSci分析でどのようなデータを扱っているのか確認しましょう。
- [Visualizing Science](./2-CitationClustering.ipynb) - 引用関係を使って論文のネットワークを作り、論文が密に疎に繋がっている様子から分野を抽出できるか検証してみましょう。
- [Research Evaluation](./3-Disruptiveness.ipynb) - 科学におけるインパクトを定量化する手法の一つとして現在ホットな"Disruption Index”を学びます。対象論文の引用ネットワークにおける親と子を含めた3世代間の引用比で論文の革新性を表現した論文を再現してみましょう。
- [Researcher Evaluation](./4-H-index.ipynb) - 研究者の評価指標として"h-index"を算出し、さらに個々の研究者のh-indexを他の変数から推定してみます。様々な交絡を考慮してより精度高く推定してみてください。