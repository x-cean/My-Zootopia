import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")
print(animals_data)

for animal in animals_data:
    if "name" in animal:
        print("Name:", animal["name"])
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print("Diet:", animal["characteristics"]["diet"])
    if "locations" in animal and len(animal["locations"]) > 0:
        print("Location:", animal["locations"][0])
    if "characteristics" in animal and "type" in animal["characteristics"]:
        print("Type:", animal["characteristics"]["type"])
    print()
