import pandas as pd
from sklearn import linear_model

df_kosong = pd.read_csv("systems/kosong.csv")
df_coklat = pd.read_csv("systems/coklat.csv")
df_keju = pd.read_csv("systems/keju.csv")

reg_kosong = linear_model.LinearRegression()
reg_coklat = linear_model.LinearRegression()
reg_keju = linear_model.LinearRegression()

reg_kosong.fit(df_kosong[['tepung', 'garam', 'ragi']], df_kosong.air)
reg_coklat.fit(df_coklat[['tepung', 'coklat', 'ragi']], df_coklat.air)
reg_keju.fit(df_keju[['tepung', 'keju', 'ragi']], df_keju.air)


def air_kosong(tepung, garam, ragi):
    return float(reg_kosong.predict([[tepung, garam, ragi]]))


def air_coklat(tepung, coklat, ragi):
    return float(reg_coklat.predict([[tepung, coklat, ragi]]))


def air_keju(tepung, keju, ragi):
    return float(reg_keju.predict([[tepung, keju, ragi]]))
