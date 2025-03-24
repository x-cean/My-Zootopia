import json


def load_data(file_path):
    """
    load data from json file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_data_string(file_path):
    """
    returning organized text as string from a json file carrying nested data structure
    """
    animal_data_text = ""
    # get the data
    animals_data = load_data(file_path)
    # loop through and collect info for each animal, update the text
    for animal in animals_data:
        if "name" in animal:
            animal_data_text += f"Name: {animal['name']}\n"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            animal_data_text += f"Characteristics: {animal["characteristics"]["diet"]}\n"
        if "locations" in animal and len(animal["locations"]) > 0:
            animal_data_text += f"Locations: {animal["locations"][0]}\n"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            animal_data_text += f"Type: {animal["characteristics"]["type"]}\n"
    # return text string
    return animal_data_text


def read_html(file_path):
    """
    read html file and return html content
    """
    with open(file_path, "r") as f:
        return f.read()


def update_animal_html(old_str, new_str):
    """
    take a html template and replace placeholder string with target data string
    """
    text = read_html("animals_template.html")
    text = text.replace(old_str, new_str)
    with open("animals.html", "w") as f:
        f.write(text)


def main():
    animals_text = generate_animal_data_string("animals_data.json")
    update_animal_html("__REPLACE_ANIMALS_INFO__", animals_text)


if __name__ == "__main__":
    main()


