import requests
from pprint import pprint

SHEET_PRICE_ENDPOINT = YOUR SHEETY ENDPOINT


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_PRICE_ENDPOINT)
        price_data = response.json()
        self.destination_data = price_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"url={SHEET_PRICE_ENDPOINT}/{city['id']}",
                                    json=new_data)
            print(response.text)

