from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# Load CSV
df = pd.read_csv("students.csv")

@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(default=None, alias="class")):
    if class_:
        filtered = df[df["class"].isin(class_)]
    else:
        filtered = df
    return {"students": filtered.to_dict(orient="records")}
