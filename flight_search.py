import requests
from flight_data import FlightData


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_APIKEY = ""

class FlightSearch:
    def get_destination(self, city):
        parameters = {
            'term': city
        }
        self.header= {
            'apikey': TEQUILA_APIKEY
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=parameters, headers=self.header)
        city_data = response.json()
        self.iatacode = city_data['locations'][0]['code']
        return self.iatacode

    def get_locations(self, origin_city_code, destination_city_code, date_from, date_to):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP"
        }
        header = {
            'apikey': TEQUILA_APIKEY
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
