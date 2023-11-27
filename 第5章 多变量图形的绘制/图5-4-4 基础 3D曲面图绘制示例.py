
"""
编写时间：2022年4月18日 18：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["axes.labelsize"] = 12
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 15
rc["xtick.major.pad"] =.5
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["font.family"] = "Times New Roman"


x=y=np.linspace(-10, 10,20)
[X, Y] = np.meshgrid(x,y)
Z = X + Y


# a）基础3D曲面图（单一颜色样式）

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X, Y, Z,ec="k",lw=.4)
ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
ax.invert_xaxis()
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-4-4 基础 3D曲面图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-4 基础 3D曲面图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）基础3D曲面图（渐变色颜色样式）

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X, Y, Z,ec="k",lw=.4,cmap=parula)
ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
ax.invert_xaxis()
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-4-4 基础 3D曲面图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-4 基础 3D曲面图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()



