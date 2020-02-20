import requests
import json
from os import getenv





base_url = 'https://immoscout-api-ji3l2ohvha-lz.a.run.app'

summary_url = '/get_summary'
page_url = '/get_list?page='
data_url = '/get_data?id='

get_summary = requests.get(base_url + summary_url,headers={"accept":"application/json","X-API-KEY":"dffbab93-44e9-41c2-bfff-6bab66c89b6c"})
if get_summary:
    print('Success!')
else:
    print('An error has occurred getting the data summary.')



total_pages = get_summary.json()["total_pages"]
total_adds = get_summary.json()["total_ads"]


i = 2
page_info = []
id_list = []
ad_list = []

temp_list = requests.get(base_url + page_url + str(i),headers={"accept": "application/json", "X-API-KEY": "dffbab93-44e9-41c2-bfff-6bab66c89b6c"})
if temp_list:
    print(temp_list.json())
    page_info.append(temp_list.json())
    x = page_info[0]['ids'][2]

    temp_data= requests.get(base_url + data_url + str(x),headers={"accept": "application/json", "X-API-KEY": "dffbab93-44e9-41c2-bfff-6bab66c89b6c"})




print('immoscout_id:=',temp_data.json()['expose.expose']['realEstate']['@id'])
if 'livingSpace' in temp_data.json()['expose.expose']['realEstate']:
    print('area_sq_m:=', temp_data.json()['expose.expose']['realEstate']['livingSpace'])
print('cnt_rooms:=',temp_data.json()['expose.expose']['realEstate']['numberOfRooms'])
if 'numberOfFloors' in temp_data.json()['expose.expose']['realEstate']:
    print('cnt_floors:=', temp_data.json()['expose.expose']['realEstate']['numberOfFloors'])
if 'floor' in temp_data.json()['expose.expose']['realEstate']:
    print('floor:=', temp_data.json()['expose.expose']['realEstate']['floor'])
print('type=',temp_data.json()['expose.expose']['realEstate']['apartmentType'])
print('has_fitted_kitchen:=',temp_data.json()['expose.expose']['realEstate']['builtInKitchen'])
print('has_lift:=',temp_data.json()['expose.expose']['realEstate']['lift'])
print('has_balcony:=',temp_data.json()['expose.expose']['realEstate']['balcony'])
print('has_garden:=',temp_data.json()['expose.expose']['realEstate']['garden'])
print('has_guest_toilet:=',temp_data.json()['expose.expose']['realEstate']['guestToilet'])
print('is_barrier_free:=',temp_data.json()['expose.expose']['realEstate']['handicappedAccessible'])
if 'heatingType' in temp_data.json()['expose.expose']['realEstate']:
    print('heating_type:=', temp_data.json()['expose.expose']['realEstate']['heatingType'])
if 'thermalCharacteristic' in temp_data.json()['expose.expose']['realEstate']:
    print('thermal_characteristic:=', temp_data.json()['expose.expose']['realEstate']['thermalCharacteristic'])
if 'totalRent' in temp_data.json()['expose.expose']['realEstate']:
    print('total_rent:=', temp_data.json()['expose.expose']['realEstate']['totalRent'])
print('calculatedTotalRent=', temp_data.json()['expose.expose']['realEstate']['calculatedTotalRent'])
print('base_rent:=', temp_data.json()['expose.expose']['realEstate']['baseRent'])
print('service_charge:=', temp_data.json()['expose.expose']['realEstate']['serviceCharge'])
if 'deposit' in temp_data.json()['expose.expose']['realEstate']:
    print('deposit:=', temp_data.json()['expose.expose']['realEstate']['deposit'])
print('city:=', temp_data.json()['expose.expose']['realEstate']['address']['city'])
print('district:=', temp_data.json()['expose.expose']['realEstate']['address']['quarter'])
print('zip_code:=', temp_data.json()['expose.expose']['realEstate']['address']['postcode'])
if 'street' in temp_data.json()['expose.expose']['realEstate']['address']:
    print('street:=', temp_data.json()['expose.expose']['realEstate']['address']['street'])
if 'houseNumber' in temp_data.json()['expose.expose']['realEstate']['address']:
    print('house_number:=', temp_data.json()['expose.expose']['realEstate']['address']['houseNumber'])
if 'wgs84Coordinate' in temp_data.json()['expose.expose']['realEstate']['address']:
    if 'longitude' in temp_data.json()['expose.expose']['realEstate']['address']['wgs84Coordinate']:
        print('lng:=',
              temp_data.json()['expose.expose']['realEstate']['address']['wgs84Coordinate']['longitude'])
    if 'latitude' in temp_data.json()['expose.expose']['realEstate']['address']['wgs84Coordinate']:
        print('lat:=',
              temp_data.json()['expose.expose']['realEstate']['address']['wgs84Coordinate']['latitude'])
if 'company' in temp_data.json()['expose.expose']['contactDetails']:
    print('company_name:=', temp_data.json()['expose.expose']['contactDetails']['company'])
if 'contact_firstname' in temp_data.json()['expose.expose']['contactDetails']:
    print('contact_firstname:=', temp_data.json()['expose.expose']['contactDetails']['firstname'])
if 'lastname' in temp_data.json()['expose.expose']['contactDetails']:
    print('contact_lastname:=', temp_data.json()['expose.expose']['contactDetails']['lastname'])
if 'salutation' in temp_data.json()['expose.expose']['contactDetails']:
    print('salutation:=', temp_data.json()['expose.expose']['contactDetails']['salutation'])
if 'email' in temp_data.json()['expose.expose']['contactDetails']['email']:
    print('email:=',temp_data.json()['expose.expose']['contactDetails']['email'])

print('phone_number:=',temp_data.json()['expose.expose']['contactDetails']['phoneNumberCountryCode'])
print('phone_number:=',temp_data.json()['expose.expose']['contactDetails']['phoneNumberAreaCode'])
print('phone_number:=',temp_data.json()['expose.expose']['contactDetails']['phoneNumberSubscriber'])
print('phone_number:=',temp_data.json()['expose.expose']['contactDetails']['phoneNumber'])
print('mobile_number:=',temp_data.json()['expose.expose']['contactDetails']['cellPhoneNumber'])
print('address_city:=',temp_data.json()['expose.expose']['contactDetails']['address']['city'])
print('address_street:=',temp_data.json()['expose.expose']['contactDetails']['address']['street'])
print('address_zip_code:=',temp_data.json()['expose.expose']['contactDetails']['address']['postcode'])
print('address_house_number:=',temp_data.json()['expose.expose']['contactDetails']['address']['houseNumber'])











