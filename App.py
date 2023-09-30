import pandas as pd

from flask import Flask, request, jsonify

app = Flask(__name__)

df_filmes = pd.read_csv("netflix_titles.csv")
