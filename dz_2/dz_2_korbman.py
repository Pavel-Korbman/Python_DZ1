'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

from pandas import DataFrame
from pandas import get_dummies

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI': lst})

# 1 вар: без get_dummies :
data.loc[data['whoAmI'] == 'human', 'human'] = True
data.loc[data['whoAmI'] != 'human', 'human'] = False
data.loc[data['whoAmI'] == 'robot', 'robot'] = True
data.loc[data['whoAmI'] != 'robot', 'robot'] = False
data_one_hot = data[['human','robot']]
print(data_one_hot.head())

# 2 вар: с использованием get_dummies :
data_one_hot_1 = get_dummies(data['whoAmI'])
print(data_one_hot_1.head())