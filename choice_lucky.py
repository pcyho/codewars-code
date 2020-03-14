import pandas as pd
from random import *

data_frame = pd.DataFrame(pd.read_csv("C:/Users/17269/Desktop/a.csv"))
list = data_frame['姓名'].to_list()
print(choice(list))
