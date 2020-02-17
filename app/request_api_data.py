import requests
import json
from os import getenv


base_url = 'https://immoscout-api-ji3l2ohvha-lz.a.run.app'

summary_url = '/get_summary'
page_url = '/get_list?page='
data_url = '/get_data?id='

#test1 = base_url + summary_url

#print(test1)

#Get the total number of pages since we have to request the data page by page.
get_summary = requests.get(base_url + summary_url,headers={"accept":"application/json","X-API-KEY":"dffbab93-44e9-41c2-bfff-6bab66c89b6c"})
if get_summary:
    print('Success!')
else:
    print('An error has occurred getting the data summary.')



total_pages = get_summary.json()["total_pages"]
total_adds = get_summary.json()["total_ads"]

#print(total_adds, total_pages)
f = open("guru99.txt","w+", encoding='utf-8')
i = 1
page_info = []
id_list = []
ad_list = []
while i <= total_pages:   # Iterate through all the pages to get the list os IDs
    temp_list = requests.get(base_url + page_url + str(i),
                        headers={"accept": "application/json", "X-API-KEY": "dffbab93-44e9-41c2-bfff-6bab66c89b6c"})
    if temp_list:
        print('Success!-List', i)
        page_info.append(temp_list.json())
        for x in page_info[i - 1]['ids']:  # Iterate through the IDs on each page
            id_list.append(x)
            temp_data= requests.get(base_url + data_url + str(x),
                           headers={"accept": "application/json", "X-API-KEY": "dffbab93-44e9-41c2-bfff-6bab66c89b6c"})
            if temp_data:
                #print('Success!-Data')
                json.dump(temp_data.json(), f, ensure_ascii=False, indent=4)
                f.write('\n')
                #ad_list.append(temp_data.json())
            else:
                print('An error has occurred getting the data piece.')

    else:
        print('An error has occurred getting the page data.')
    #print(page_info[i-1])
    i+=1

print("Number of ads predicted=",total_adds, "number of actual ads obtained=", len(id_list))



f.close()



