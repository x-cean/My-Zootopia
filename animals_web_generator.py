import json


FILE_PATH = "animals_data.json"


def load_data(file_path):
    """
    load data from json file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_and_display_skin_types_from_data(animals_list):
    """
    receives a list of animal info and get all skin types
    """
    skin_types = []
    for animal in animals_list:
        # will only take the animals with skin type info into account
        if "characteristics" in animal and "skin_type" in animal["characteristics"]:
            if animal["characteristics"]["skin_type"].lower().strip() not in skin_types:
                skin_types.append(animal["characteristics"]["skin_type"].lower().strip())
    print("Hi! There are {} skin types: ".format(len(skin_types)))
    for skin in skin_types:
        print(skin)
    print()
    return skin_types


def get_skin_type_from_user(skin_types):
    """
    ask user to input valid skin type
    """
    while True:
        skin_type = input("Enter a skin type from above to display the animals (Enter 0 to display all): ")
        if skin_type.lower().strip() in skin_types:
            return skin_type.lower().strip()
        elif skin_type.strip() == "0":
            return skin_type.strip()
        else:
            print("Please enter a valid skin type.")


def filter_animal_skin_type(skin_type, animal_list):
    """
    receives a list of data and a skin type keyword, filter out animal with that skin type
    """
    filtered_animal_list = []
    for animal in animal_list:
        if "characteristics" in animal and "skin_type" in animal["characteristics"]:
            if skin_type == animal["characteristics"]["skin_type"].lower().strip():
                filtered_animal_list.append(animal)
    return filtered_animal_list


def serialize_animal(animal_obj):
    """
    receives a dictionary and return its info as formatted html text
    """
    animal_data_text = "<li class='cards__item'>"
    if "name" in animal_obj:
        animal_data_text += f"<div class='card__title'>{animal_obj["name"]}</div>\n"
    animal_data_text += "<div class='card__text'>\n<ul>"
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        animal_data_text += f"<li><strong>Diet: </strong>{animal_obj["characteristics"]["diet"]}</li>\n"
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        animal_data_text += f"<li><strong>Location: </strong>{animal_obj["locations"][0]}</li>\n"
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        animal_data_text += f"<li><strong>Type: </strong>{animal_obj["characteristics"]["type"]}</li>\n"
    if "characteristics" in animal_obj and "slogan" in animal_obj["characteristics"]:
        animal_data_text += f"<li><strong>Slogan: </strong>{animal_obj["characteristics"]["slogan"]}</li>\n"
    animal_data_text += "</ul></div></li>"
    return animal_data_text


def generate_animal_data_string(animals_data):
    """
    returning organized text as string from a json file carrying nested data structure
    """
    output = ""
    # loop through and collect info for each animal, update the text
    for animal in animals_data:
        output += serialize_animal(animal)
    # return text string
    return output


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
    animals_data = load_data(FILE_PATH)
    skin_types = get_and_display_skin_types_from_data(animals_data)
    skin_type = get_skin_type_from_user(skin_types)
    if skin_type == "0":
        animals_text = generate_animal_data_string(animals_data)
    else:
        filtered_animals_data = filter_animal_skin_type(skin_type, animals_data)
        animals_text = generate_animal_data_string(filtered_animals_data)
    update_animal_html("__REPLACE_ANIMALS_INFO__", animals_text)


if __name__ == "__main__":
    main()
