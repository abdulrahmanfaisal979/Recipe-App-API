import pandas as pd
from fastapi import FastAPI
import helper_fun as h

app = FastAPI()

df = pd.read_csv("Book1.csv")


@app.post("/filter")
def filter_recipes(new_data: dict):

    filter_option = new_data["filter_option"]
    filter_value = new_data["filter_value"]

    result = h.filter_recipe(df,filter_option,filter_value)

    return {"result": result.to_dict()}