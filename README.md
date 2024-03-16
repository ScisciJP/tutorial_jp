# ScisciJP 2024 Tutorial

Scisci分野の論文およびコードのチュートリアルを、2024年の3/17開催の[Science of Science研究会](https://sciscijp.github.io/scisciconfJP2024/)の前日イベントとして開催します。

実際のデータを分析することで、SciSciの研究内容と着眼点や手法の限界について学びます。OpenAlexという無料のデータベースを利用し、Google Colabでコードを実装しますので、ブラウザがあればどのような環境でも動作します。

- [1. Getting Started:データへのアクセスと基礎分析](./1-GettingStarted.ipynb) 
     - Science of science でどのようなデータを取り扱うのか、”Open Alex”というサービスを使っていくつか分析する中で確認しましょう。
     - [colab Link](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/1-GettingStarted.ipynb)

- [2. Visualizing Science:特定の学術分野の分類と可視化による理解](./2_CitationClustering.ipynb) 
     - 特定の学術分野の論文を抽出し、引用関係を使って論文のネットワークを作り、論文が密に疎に繋がっている様子から分野を抽出できるか検証してみましょう。
     - [colab Link](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/2_CitationClustering.ipynb)

- [3. Research Evaluation by Disruptiveness index:トップ論文のD指標の再現](./2_CitationClustering.ipynb) 
     - 研究者評価の指標として、科学におけるインパクトを定量化する手法の一つとして現在ホットな"Disruption Index”を学びます。対象論文の引用ネットワークにおける親と子を含めた3世代間の引用比で論文の革新性を表現した論文を再現してみましょう。
     - [colab Link](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/3-Disruptiveness.ipynb)

- [4. Researcher Evaluation: 被引用による研究者の評価と将来予測、その他の諸々の自由タスク](./4-H-index.ipynb)
     - 研究者の評価指標として、"h-index"を算出し、さらに個々の研究者のh-indexを他の変数から推定してみます。様々な交絡を考慮してより精度高く推定してみてください。
     - [colab Link](https://colab.research.google.com/github/ScisciJP/scisciJP2024_tutorial/blob/main/4-H-index.ipynb)


※それぞれの章は概ね独立していますので、好きな章から試してください。


## チュートリアル委員
 - 三浦 千哲 (東京大学)
 - 神楽坂 やちま (東京大学)

## コーディング
 - 1章: 三浦 千哲 (東京大学)
 - 2章: 浅谷 公威 (東京大学), 三浦 千哲 (東京大学),  原田 啓矢 (東京大学)
 - 3章: 神楽坂 やちま (東京大学)
 - 4章: 神楽坂 やちま (東京大学), 三浦 千哲(東京大学), 王 思源 (東京大学)
