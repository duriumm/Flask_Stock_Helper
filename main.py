import json
from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse
import csv
import pandas as pd


app = Flask(__name__)
api = Api(app)

stock_put_args = reqparse.RequestParser()
stock_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
stock_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
stock_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)


videos = {}

def abortFunc(video_id):
  if video_id not in videos:
    abort("video id is not valid)")

class StockMarketCalculator(Resource):
  def get(self):
    # TODO: Read the csv and return the data as JSON. (Where should the csv be located?)
    csv_data = pd.read_csv(r'C:\Users\lasse\LocalDocuments\Flask_stock\Flask_Stock_Helper\data[6596].csv', sep=';')
    print(csv_data.columns)
    print(csv_data.Date)
    print(csv_data.Kod)
    print(csv_data.Kurs)
    print(f"Amount of rows is: {len(csv_data)}")

 
    # csv_data = csv_data.set_index('index')
    csv_data = csv_data.to_dict(orient='index')

    print(csv_data)
    return csv_data

  def post(self):
    # TODO: Open the csv and add data to it
    return {"data": "We did post"}

  def put(self, date, kod, kurs):
    put_df = pd.DataFrame({
      "Date": "2017-11-11",
      "Kod": "XXX",
      "Kurs": "699"
    })
    print(f"PUT df is: {put_df}")
    csv_data = pd.read_csv(r'C:\Users\lasse\LocalDocuments\Flask_stock\Flask_Stock_Helper\data[6596].csv', sep=';',names=["Date","Kod","Kurs"])
    # csv_data.to_csv('my_csv.csv', mode='a', header=False)
    # requests.put(BASE, {"name": "Lasse name", "views": 102, "likes": 10})
    # args = video_put_args.parse_args()
    # videos[video_id] = args
    # return videos[video_id], 201 # returns what we put in


api.add_resource(StockMarketCalculator, "/stocklist")


# @app.route('/')
# def hello():
#   return "hello mate"


if __name__ == '__main__':
  app.run(debug=True)