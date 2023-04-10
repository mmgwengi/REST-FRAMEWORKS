import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


import warnings
warnings.filterwarnings("ignore")

dat_raw=pd.read_csv(Path('DATA\\CO2 Emissions_Canada.csv'))
dat_raw.head()

#subset not only a few columns
dat_raw.columns

dat = dat_raw[['Engine Size(L)','Cylinders','Fuel Consumption Comb (L/100 km)','CO2 Emissions(g/km)']]

dat.head()

X = dat[['Engine Size(L)','Cylinders','Fuel Consumption Comb (L/100 km)']]
y = dat[['CO2 Emissions(g/km)']]

#split into train and test to avoid overfitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

regressor = LinearRegression()
#Fitting model with trainig data
regressor.fit(X_train, y_train)

with Path('WebApps\\Flask_CarbonDioxide_emission\\model.pkl').open('wb') as fp:
    pickle.dump(regressor,fp)
    
    
with Path('WebApps\\Flask_CarbonDioxide_emission\\model.pkl').open('wb') as fp:
    pickle.dump(regressor,fp)    
    
#Loading model to compare the results

model = pickle.load(open('C:\\Users\\marth\\Data Science\\Machine Learning\\WebApps\\Flask_CarbonDioxide emission\\model.pkl','rb'))
#fuel emission based on these values
print(model.predict([[4, 9, 10.7]]))