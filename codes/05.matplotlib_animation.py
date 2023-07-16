import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# 데이터 생성
data = np.array([20, 30, 40, 50, 60, 70, 80, 90])

# Figure 생성 
fig, ax = plt.subplots(figsize=(12, 8))

# 막대 그래프 그리기
bar = ax.bar(np.arange(len(data)), data)

# Animation function 정의
def animate(i):
  rotation = (i+1)*10
  bar[-1].set_color('r')
  for rect, h in zip(bar, data):
      rect.set_height(np.sin(np.pi / 2 * (h + rotation) / max(data)) * max(data) * 0.8 + max(data) * 0.1)
  return tuple(bar)

# Animation 객체 생성
ani = animation.FuncAnimation(fig, animate, frames=90, interval=50)

# mp4 파일로 저장
ani.save('animating_bar.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

# Jupyter Notebook 출력
HTML(ani.to_jshtml())
