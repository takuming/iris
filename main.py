import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# データの読み込み
iris_data = pd.read_csv("iris.csv")

# 特徴量とターゲットの分割
X = iris_data.drop("species", axis=1)
y = iris_data["species"]

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルのトレーニング
model = RandomForestClassifier()
model.fit(X_train, y_train)

# モデルの保存
joblib.dump(model, "trained_model.pkl")

from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# モデルのロード
model = joblib.load("trained_model.pkl")

# APIエンドポイントの作成
@app.post("/predict")
async def predict(data: dict):
    # 入力データの準備
    input_data = pd.DataFrame([data])
   
    # 予測の実行
    prediction = model.predict(input_data)
   
    return {"prediction": prediction.tolist()}