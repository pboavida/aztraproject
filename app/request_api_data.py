import requests
import json


#setup the links that are going to be used for the api requests
base_url = 'https://immoscout-api-ji3l2ohvha-lz.a.run.app'

summary_url = '/get_summary'
page_url = '/get_list?page='
data_url = '/get_data?id='



#Get the total number of pages since we have to request the data page by page.
get_summary = requests.get(base_url + summary_url,headers={"accept":"application/json","X-API-KEY":"dffbab93-44e9-41c2-bfff-6bab66c89b6c"})
if get_summary:
    print('Success!')
else:
    print('An error has occurred getting the data summary.')



total_pages = get_summary.json()["total_pages"]
total_adds = get_summary.json()["total_ads"]

#create the file where we will store the data
f = open("raw_data.dat","w+", encoding='utf-8')
i = 1
page_info = []
id_list = []
#ad_list = []
while i <= total_pages:   # Iterate through all the pages to get the list os IDs
    temp_list = requests.get(base_url + page_url + str(i),
                        headers={"accept": "application/json", "X-API-KEY": "dffbab93-44e9-41c2-bfff-6bab66c89b6c"}) #all the isntances of the api key should be replaced by a variable that stores the key
    if temp_list:
        print('Success!-List', i)
        page_info.append(temp_list.json())
        for x in page_info[i - 1]['ids']:  # Iterate through the IDs on each page
            id_list.append(x)
            temp_data= requests.get(base_url + data_url + str(x),
                           headers={"accept": "application/json", "X-API-KEY": "dffbab93-44e9-41c2-bfff-6bab66c89b6c"})
            if temp_data:
                #print('Success!-Data')
                json.dump(temp_data.json(), f, ensure_ascii=False, indent=4) #print data to file, the indent is for human readability but can be removed and each line of the file will correspond to one ad
                f.write('\n')

                #ad_list.append(temp_data.json()) #if the only purpose of getting the data is to dump them on a the file, then the array won't be needed as we can do it one by one
            else:
                print('An error has occurred getting the data piece.')

    else:
        print('An error has occurred getting the page data.')
    i+=1

print("Number of ads predicted=",total_adds, "number of actual ads obtained=", len(id_list)) # in tests the 2 numbers don't seem to match, would require further investigation


f.close()



