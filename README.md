#### 한글 처리 : [link](./refer/README.md)
### more package visuallization
- Mito : https://www.trymito.io/
- Plotly : https://plotly.com/
- Lux(A Python API for Intelligent Visual Discovery) : https://github.com/lux-org/lux
- Bokeh : [ipynb](https://colab.research.google.com/drive/1k1JdZG2VMrNxcW3gku9-C20OO8t6vEZW#scrollTo=w8eaAUE5suk8)

### need to learn more(사전 학습 : Numpy, Pandas)
- [Analyze and Visualize URLs with Network Graph](https://towardsdatascience.com/analyze-and-visualize-urls-with-network-graph-ee3ad5338b69)
- [변량(Variance)별 분석 도구(Graph, Plot, Chart)](https://dbrang.tistory.com/1208)
- [4편. Seaborn 그래프 종류 총 정리(ft. Distribution plots)](https://coding-kindergarten.tistory.com/132)
- Matplotlib [파이썬 코딩 무료 강의 (활용편5) 2:55:00~end](https://youtu.be/PjhlUzp_cU0)

## 시각화 사례
- 서울시 연간 기온변화 시각화(from sesac) : 하나 Sample(1950년 대)로 시연 후 전체는 실습

#### 강의 전체 흐름 (사전 필요 : pandas.groupby(), pandas.pivot())
| 주제 | 주요 항목 | dataset | 작성 | 참조 |
| matplotlib | plot, bar, scatter | :---: |sesac(일부 먼저 작성 seaborn과 비교):seaborn 차트 그리기|sesac:파이썬 데이터 시각화 시작하기, 그래프 스타일링, 데이터의 분포와 비율을 파악하기 위한 그래프, 데이터의 관계를 파악하거나 크기를 비교하기 위한 그래프|
| seaborn | lineplot, barplot, scatterplot, countplot | :---: |:---: |sesac:seaborn 차트 그리기 |
| matplotlib | subplot, add_axesplot | :---: |:---: |sesac:서브플롯 그리기 |
|networkx|?, pagerank| |

#### 대략 상세 내용
| 주제 | 주요 항목 | 참조 |
| --- | --- | :---: |
|matplotlib 기본|한글 처리,axes,tick,legend,markder,figure,savefig,text| |
|matplotlib more|여러 데이터,막대|[in ipynb](./codes/03_visualization_Matplotlib.ipynb) |
|subplot|subplot|seaborn.dataset?|
|subplot|add_axesplot()|[video](sesac_visuallization_subplot_2_.mov)|
|seaborn|barplot(estimator, hue, ci=None, palette) - dataset tips| [sassek](https://sesac.seoul.kr/):seaborn-막대그래프 |
|seaborn|scatterplot(hue, size, alpha) - dataset tips|[sassek](https://sesac.seoul.kr/):데이터의 관계 파악을 위한 scatterplot|
|seaborn|scatterplot(hue, size, alpha) - dataset tips|[sassek](https://sesac.seoul.kr/):데이터의 추세를 표현하는 lineplot|
|seaborn|lineplot(estimator, ci=None, marker, ls, hue) - dataset flight|[sassek](https://sesac.seoul.kr/):데이터의 추세를 표현하는 lineplot|
|seaborn|countplot(), ?rugplot, displot(bins, rug, hue, kde), boxplot, violinplot, stripplot, swarmplot|dataset titanic, iris|


