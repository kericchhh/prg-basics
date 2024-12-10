countries = [
{"name":"Poland", "population":38000000},
{"name":"USA", "population":346219880},
{"name":"Japan", "population":123753041},
{"name":"Germany", "population":84552242},
{"name":"Italy", "population":59342867}
]

print("COUNTRY  POPULATION")
for country in countries:
    print(f"{country['name']:<8} {country['population']}")