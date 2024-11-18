# Exercise 1

dict1: dict[str, str] = {"name": "Israel", 'birth': 1948, 'population_millions': 9.3, 'capital': 'Jerusalem',
                         'language': 'Hebrew',
                         'cities': ['Jerusalem', 'Tel Aviv', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod'],
                         'currency': 'ILS', 'area_Kilometer': 22145, 'gdp_billion': 450}
print(dict1.get("capital", None))
print(list(dict1.keys()))
print(list(dict1.values()))
for key, value in dict1.items():
    print(f"{key}:{value}")

dict2: dict[str, str] = dict1.copy()
print(dict2.pop('gdp_billion'))

dict3: dict[str, str] = dict.fromkeys(dict1.keys())
for key in dict3.keys():
    if key == "cities":
        dict3[key] = [input(f"Enter the {key}: ") for _ in range(3)]
    else:
        dict3[key] = input(f"Enter the {key}: ")
print(dict3)


# Exercise 2
def last_word_length(str1: str) -> int:
    list1: list[str] = str1.split()
    return len(list1[-1])


print(last_word_length('luffy is still joyboy'))
