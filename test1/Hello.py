import numpy as np
import pandas as pd
s=pd.Series([1,3,5,np.nan,6,8])
print(s)
dates=pd.date_range('20200830',periods=6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index = dates, columns = list('ABCD'))
print(df)
df2 = pd.DataFrame({'A':1,'B':pd.Series(1,index=list(range(4)),dtype='float32')})
print(df2)