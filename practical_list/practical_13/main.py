import matplotlib.pyplot as plt
import pandas_datareader as pdr
import datetime

goog = pdr.get_data_yahoo('GOOG',
                          start=datetime.datetime(2010, 2, 5),
                          end=datetime.datetime(2020, 9, 3))
goog['Close'].plot()
plt.title('GOOGLEEEEE Stock Prices')
plt.xlabel(' THE Year')
plt.ylabel('THE Price in $')
plt.show()
