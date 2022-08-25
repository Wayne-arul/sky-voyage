#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import *
from notification_manager import NotificationManager

ORIGIN_CITY = "LON"
from_date = datetime.now().date()
to_date = from_date + timedelta(days=6 * 30)

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_sheet_data()


    # for i in sheet_data:
    #     if i['iataCode'] == '':
    #         i['iataCode'] = "TESTING"
    # data_manager.put_sheet_data()
    # print(sheet_data)

if sheet_data[0]['iataCode'] == '':
    for i in sheet_data:
        city = i['city']
        iataCode = flight_search.get_destination(city)
        i['iataCode'] = iataCode
    data_manager.update_sheet_data()
#
# print(sheet_data)

city = sheet_data[0]['iataCode']
# print(city)

for destination in sheet_data:
    location = flight_search.get_locations(ORIGIN_CITY, destination['iataCode'], from_date, to_date)
    if location.price < destination['lowestPrice']:
        notification_manager.send_sms(
            f"Low price alert! Only £{location.price} to fly from {location.origin_city}-{location.origin_airport} to {location.destination_city}-{location.destination_airport}, from {location.out_date} to {location.return_date}.")

















