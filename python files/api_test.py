# import requests

# url = "https://covid-19-statistics.p.rapidapi.com/regions"

# headers = {
# 	"x-rapidapi-key": "a27d25665dmsh332b587ec391425p11426fjsn2121477ec4cc",
# 	"x-rapidapi-host": "covid-19-statistics.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# # print(response.json())
# r=response.json()
# # print(r["data"])
# for i in r["data"]:
#     # print(i)
#     for d in i:
#         # print(d)
#         if d == "iso":
#             print(d , ":" ,i[d])
#         # for key in d:
#             # print(key)

# # Example
# # a = [{"a" : "A","b":"B"},{"a" : "C","d":"D"}]
# # for i in a:
# #     for j in i:
# #         if j == "a":
# #             print(i[j])




#<==========================================================================================================================


# import requests

# url = "https://cars-by-api-ninjas.p.rapidapi.com/v1/cars"

# querystring = {"model":"corolla"}         #works according to model name   (try for other "civic" model name)

# headers = {
# 	"x-rapidapi-key": "a27d25665dmsh332b587ec391425p11426fjsn2121477ec4cc",
# 	"x-rapidapi-host": "cars-by-api-ninjas.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

#<==========================================================================================================================


import requests

url = "https://ai-text-to-image-generator-flux-free-api.p.rapidapi.com/aaaaaaaaaaaaaaaaaiimagegenerator/quick.php"

payload = {
	"prompt": "say no to drugs in creative way",
	"style_id": 4,
	"size": "1-1"
}
headers = {
	"x-rapidapi-key": "a27d25665dmsh332b587ec391425p11426fjsn2121477ec4cc",
	"x-rapidapi-host": "ai-text-to-image-generator-flux-free-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())



