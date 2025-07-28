# import requests

# url = "https://weather-api167.p.rapidapi.com/api/weather/current"

# querystring = {"place":"Amritsar","units":"standard","lang":"en","mode":"json"}

# headers = {
# 	"x-rapidapi-key": "5d2f807911msh14b6502e0b1b4dep1b7543jsn52cff6c5411d",
# 	"x-rapidapi-host": "weather-api167.p.rapidapi.com",
# 	"Accept": "application/json"
# }

# response = requests.get(url, headers=headers, params=querystring)

# # print(response.json())
# var=response.json()
# # print(var["main"])
# print(var["summery"])




# import requests

# url = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat"

# querystring = {"noqueue":"1"}

# payload = {
# 	"message": "What are common brain tumors?",
# 	"specialization": "neurosurgery",
# 	"language": "en"
# }
# headers = {
# 	"x-rapidapi-key": "a27d25665dmsh332b587ec391425p11426fjsn2121477ec4cc",
# 	"x-rapidapi-host": "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers, params=querystring)

# print(response.json())
# a=response.json()
# # print(a["message"])


# import requests

# while True:
#     a=input("enter the question or type exit to exit the program ")
#     if a=="exit":
#         print("bye")
#         break
#     else:
#         url = "https://copilot5.p.rapidapi.com/copilot"

#         payload = {
#             "message": a,
#             "conversation_id": None,
#             "mode": "CHAT",
#             "markdown": True
#         }
#         headers = {
#             "x-rapidapi-key": "5d2f807911msh14b6502e0b1b4dep1b7543jsn52cff6c5411d",
#             "x-rapidapi-host": "copilot5.p.rapidapi.com",
#             "Content-Type": "application/json"
#         }

#         response = requests.post(url, json=payload, headers=headers)

#         # print(response.json())
#         x=response.json()
#         print(x["data"]["message"])



# import requests

# url = "https://ai-text-to-image-generator-flux-free-api.p.rapidapi.com/aaaaaaaaaaaaaaaaaiimagegenerator/quick.php"

# payload = {
# 	"prompt": "Narinder modi the Prime Minister of India marring with Giorgia Meloni the Prime Minister of Italy.",
# 	"style_id": 2,
# 	"size": "1-1"
# }
# headers = {
# 	"x-rapidapi-key": "5d2f807911msh14b6502e0b1b4dep1b7543jsn52cff6c5411d",
# 	"x-rapidapi-host": "ai-text-to-image-generator-flux-free-api.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.json())





# import requests

# url = "https://movies-ratings2.p.rapidapi.com/ratings"

# querystring = {"id":"tt0111161"}

# headers = {
# 	"x-rapidapi-key": "a27d25665dmsh332b587ec391425p11426fjsn2121477ec4cc",
# 	"x-rapidapi-host": "movies-ratings2.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


# import requests

# url = "https://covid-19-statistics.p.rapidapi.com/regions"

# headers = {
# 	"x-rapidapi-key": "a27d25665dmsh332b587ec391425p11426fjsn2121477ec4cc",
# 	"x-rapidapi-host": "covid-19-statistics.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())