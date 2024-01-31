import requests

class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/4bb3a7097948d0ad5e777b0275d0a87r/flightDeals/prices"
        self.auth_key = ""
        self.header = {
            "Authorization": self.auth_key
        }

    def get_sheet_data(self):
        self.response = requests.get(url=self.endpoint, headers=self.header)
        data = self.response.json()
        self.destination_data = data['prices']
        return self.destination_data


    def update_sheet_data(self):
        for i in self.destination_data:
            json_data = {
                'price': {
                    'iataCode': i['iataCode']
                }
            }
            self.response = requests.put(
                url=f"{self.endpoint}/{i['id']}",
                json=json_data,
                headers=self.header)
            print(self.response.text)

