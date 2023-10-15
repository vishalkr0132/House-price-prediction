import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

def ml_model(bath, balcony, total_sqft_int, bhk, price_per_sqft, area_type, availability, location):
    
  df = pd.read_csv("./home/data.csv")

  df = df.drop(['Unnamed: 0'], axis=1)

  X = df.drop("price", axis=1)
  y = df['price']

  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 51)

  sc = StandardScaler()
  sc.fit(X_train)
  X_train= sc.transform(X_train)
  X_test = sc.transform(X_test)

  def rmse(y_test, y_pred):
    return np.sqrt(mean_squared_error(y_test, y_pred))

  rfr = RandomForestRegressor()
  rfr.fit(X_train,y_train)
  rfr_score=rfr.score(X_test,y_test)
  rfr_rmse = rmse(y_test, rfr.predict(X_test))

  def predict_house_price(model,bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location):
    x =np.zeros(len(X.columns))
    x[0]=bath
    x[1]=balcony
    x[2]=total_sqft_int
    x[3]=bhk
    x[4]=price_per_sqft

    if "availability"=="Ready To Move":
      x[8]=1

    if 'area_type'+area_type in X.columns:
      area_type_index = np.where(X.columns=="area_type"+area_type)[0][0]
      x[area_type_index] =1

    if 'location_'+location in X.columns:
      loc_index = np.where(X.columns=="location_"+location)[0][0]
      x[loc_index] =1

    x = sc.transform([x])[0] 
    return model.predict([x])[0]
  output = predict_house_price(model=rfr, bath=bath,balcony=balcony,total_sqft_int=total_sqft_int,bhk=bhk,price_per_sqft=price_per_sqft,area_type=area_type,availability=availability,location=location)
  return output