import os
from flask import Flask
from flask_restful import Api, Resource
import pandas as pd
from IPython.display import display
root_path = os.path.dirname(__file__)
import utils
print("ROOT PATH" + root_path)
app = Flask(__name__)
api = Api(app)

print(utils)

class StockMarketCalculator(Resource):

  winners_dict = {
    'Winners':[ 

    ]
  }

  def calculate_todays_stockmarket_winners(self):
    print("winners are")

  def calculate_percentage_diff(self, old_value, new_value):
    percent_diff = (float(new_value - old_value) / abs(old_value)) * 100 # Abs to handle negative values
    return percent_diff


  def get(self):
    config = utils.get_config()
    csv_data = pd.read_csv(config["csv_path"], sep=';')
    print("\nRegular values")
    display(csv_data)
    first_unique_values = csv_data.sort_values('Date').drop_duplicates(['Kod']) ######

    print("\nFIRST UNIQUE VALUES")
    display(first_unique_values)

    last_unique_values = csv_data.sort_values('Date', ascending=False).drop_duplicates(['Kod'])
    print("\LAST UNIQUE VALUES")
    display(last_unique_values)

    rank = 0
    for index, row in last_unique_values.iterrows():
      stock_name = row['Kod']
      last_unique_value = row['Kurs']
      first_unique_value = first_unique_values.loc[first_unique_values['Kod'] == row['Kod'], 'Kurs'].values[0]
      percentage_diff_value = self.calculate_percentage_diff(first_unique_value, last_unique_value)
      print(f"First unique for {row['Kod']}: {first_unique_value}")
      print(f"Last unique for {row['Kod']}: {last_unique_value}")
      print(f"percentage_diff for {row['Kod']}: {round(percentage_diff_value, 2)}")
      print()


      self.winners_dict["Winners"].append({"rank": 0, "name": stock_name, "percent": round(percentage_diff_value, 2), "latest": last_unique_value })

    self.winners_dict["Winners"] = sorted(self.winners_dict["Winners"], key=lambda d: d['percent'], reverse=True) 

    # for stock, index in self.winners_dict["Winners"]:
    #   self.winners_dict["Winners"]
    #   print(stock)

    # Set rank and remove other than top 3
    for index, stock in enumerate(self.winners_dict["Winners"]):
      if index < 3:
        print(f"WE ARE AT INDEX: {index}, FOR STOCK: {stock}")
        print(f"LENGTH OF LIST: {len(self.winners_dict['Winners'])}")

        print(f"type rank: {type(rank)}")
        self.winners_dict["Winners"][index]["rank"] = index + 1

    # Delete objects over len 3
    for obj in self.winners_dict["Winners"]:
      if len(self.winners_dict["Winners"]) == 3:
        print("length 3, returning")
        break
      else:
        del self.winners_dict["Winners"][-1]


    print(f"LENGTH OF LIST after: {len(self.winners_dict['Winners'])}")

    # # self.calculate_todays_stockmarket_winners()

    print(self.winners_dict)
    return self.winners_dict


api.add_resource(StockMarketCalculator, "/stocklist")

if __name__ == '__main__':
  app.run(debug=True)