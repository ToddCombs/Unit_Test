
from urllib.parse import quote

import numpy as np
import pandas as pd

xlsx = pd.read_excel(r"C:\Users\admin\PycharmProjects\Unit_Test\demo\Locust_demo\10000_w.xlsx", engine='openpyxl', header=None, usecols=[1])
data = xlsx.head(10001)
print(str(data))