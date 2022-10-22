import os
from flask import Flask
from flask_restful import Api, Resource
import pandas as pd
from IPython.display import display
root_path = os.path.dirname(__file__)
import utils
app = Flask(__name__)
api = Api(app)


class StockMarketCalculator(Resource):

  winners_dict = { 'Winners':[] }
  config = utils.get_config()
  
  def calculate_percentage_diff(self, old_value, new_value):
    percent_diff = (float(new_value - old_value) / abs(old_value)) * 100 # Abs to handle negative values
    return percent_diff

  def calculate_todays_stockmarket_winners(self):
    # Get the first and last unique values into two separate dataframes
    csv_data = pd.read_csv(self.config["csv_path"], sep=';')
    first_unique_values = csv_data.sort_values('Date').drop_duplicates(['Kod']) 
    last_unique_values = csv_data.sort_values('Date', ascending=False).drop_duplicates(['Kod'])

    # Add calculated data from both dataframes into the winners dictionary
    for index, row in last_unique_values.iterrows():
      stock_name = row['Kod']
      last_unique_value = row['Kurs']
      first_unique_value = first_unique_values.loc[first_unique_values['Kod'] == row['Kod'], 'Kurs'].values[0]
      percentage_diff_value = self.calculate_percentage_diff(first_unique_value, last_unique_value)
      print(f"\nFirst unique for {row['Kod']}: {first_unique_value}") ## TODO: Remove print
      print(f"Last unique for {row['Kod']}: {last_unique_value}")     ## TODO: Remove print
      print(f"percentage_diff for {row['Kod']}: {round(percentage_diff_value, 2)}") ## TODO: Remove print

      self.winners_dict["Winners"].append({"rank": 0, "name": stock_name, "percent": round(percentage_diff_value, 2), "latest": last_unique_value })

    # Sort winners list based on percent and keep top three only
    self.winners_dict["Winners"] = sorted(self.winners_dict["Winners"], key=lambda d: d['percent'], reverse=True)[:3]

    # Set rank for the remaining data fields
    for index, stock in enumerate(self.winners_dict["Winners"]):
        self.winners_dict["Winners"][index]["rank"] = index + 1

  def get(self):
    # Reset winners_dict 
    self.winners_dict = { 'Winners':[] }

    # Add top 3 winners of today to the winners_dict 
    self.calculate_todays_stockmarket_winners()

    print(self.winners_dict) ## TODO: Remove print
    # Return serialized winners_dict as JSON
    return self.winners_dict


api.add_resource(StockMarketCalculator, "/stocklist")

if __name__ == '__main__':
  app.run(debug=True)