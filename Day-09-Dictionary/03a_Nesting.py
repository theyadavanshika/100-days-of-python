capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nested List in Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : [ "Stuttgart", "Berlin"]
}

#print Lille
print(travel_log["France"][1])

# 2D list -> list under list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

