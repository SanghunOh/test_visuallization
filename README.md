#### 시각화
| 주제 | 주요 항목 | 참조 |
| --- | --- | :---: |
| 기본과 꺾은선 그래프 | matplotlib, seaborn, plotly||
| 막대 그래프 | matplotlib, seaborn, plotly||
| 누적 막대 그래프 | matplotlib, seaborn, plotly||
## ?
|matplotlib 기본|한글 처리,axes,tick,legend,markder,figure,savefig,text| |
|matplotlib more|여러 데이터,막대| |
|seaborn|barplot()| |

> matplotlib OS별 한글 처리
```
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':  # Windows
    font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
    rc('font', family=font_name)
else :  # MAC
    rc('font', family='AppleGothic')
```
> matplotlib '-' 기호 표시
```
from matplotlib import rcParams
rcParams['axes.unicode_minus'] = False
```
> pandas 최대 변수/행 수 확인
pandas.options.display.max_info_columns
pandas.options.display.max_info_rows
