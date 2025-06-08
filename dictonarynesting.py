# travel_log = {
#     "france" : ["paris","Lille","Dijon"],
#     "germany" : ["stuttgrate", "Berlin"]
# }

# print(travel_log["france"][1])

# nested_list = ["A","B",["c","d"]]
# print(nested_list[2][1])


travel_log = {
"France":{
    "cities_visited":["Paris","Lille","Dijon"],
    "total_visits":12
},
"Germany":{
    "cities_visited":["Berlin","Hamberg","Stuttgrate"],
    "total_visits":5
},
}

print(travel_log["Germany"]["cities_visited"][2])