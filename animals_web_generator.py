import json


def load_data(file_path):
    """
    load data from json file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    receives a dictionary and return its info as formatted html text
    """
    animal_data_text = "<li class='cards__item'>"
    if "name" in animal_obj:
        animal_data_text += f"<div class='card__title'>{animal_obj["name"]}</div>\n"
    animal_data_text += "<p class='card__text'>"
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        animal_data_text += f"<strong>Diet: </strong>{animal_obj["characteristics"]["diet"]}<br/>\n"
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        animal_data_text += f"<strong>Location: </strong>{animal_obj["locations"][0]}<br/>\n"
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        animal_data_text += f"<strong>Type: </strong>{animal_obj["characteristics"]["type"]}<br/>\n"
    animal_data_text += "</p></li>"
    return animal_data_text


def generate_animal_data_string(file_path):
    """
    returning organized text as string from a json file carrying nested data structure
    """
    output = ""
    # get the data
    animals_data = load_data(file_path)
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
    animals_text = generate_animal_data_string("animals_data.json")
    update_animal_html("__REPLACE_ANIMALS_INFO__", animals_text)


if __name__ == "__main__":
    main()
