import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置tushare的token
ts.set_token('19daf5d0248695483d961699537e768560bf359f240a0d4c084b08c1')

# 初始化tushare接口
pro = ts.pro_api()

# 获取股票数据
# start_date--开始日期，为"%Y%m%d"格式
# end_date--结束日期，为"%Y%m%d"格式
df = pro.daily(ts_code='300491.SZ', start_date='20230101', end_date='20230308')

# 计算移动平均线
df['MA'] = df['close'].rolling(window=10).mean()

# 计算RSI指标
delta = df['close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean().abs()
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

# 策略实现
df['Signal'] = np.where(df['close'] > df['MA'], 1, 0)
df['Signal'] = np.where(df['RSI'] < 30, 1, 0)
df['Position'] = df['Signal'].diff()

# 计算收益率
df['Returns'] = df['close'].pct_change() * df['Position'].shift(1)

# 计算累计收益率
df['Cumulative_Returns'] = (1 + df['Returns']).cumprod()

# 绘制图表
plt.figure(figsize=(10, 5))
plt.plot(df['trade_date'], df['Cumulative_Returns'])
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()