import data_fetcher

def serialize_animal(animal_obj, animal_name):
    output = ''
    characteristics = animal_obj.get('characteristics', {})
    animal_type = characteristics.get('type')
    if animal_type:
        output += '<li class="cards__item">\n'
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
        output += f'<p class ="card__text">\n'
        output += f'<strong> Diet: </strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
        output += f'<strong> Location: </strong> {animal_obj["locations"][0]}<br/>\n'
        output += f'<strong> Type: </strong> {animal_type}<br/>\n'
        output += '</p>\n'
        output += '</li>\n'
    if len(animal_obj) == 0:
        output += f' <h2> The animal {animal_name} does not exist. </h2>\n'
    return output

def html_load():
    """ Loads a html template file """
    with open('animals_template.html', "r") as template_file:
        template_content = template_file.read()
    return template_content

def html_store(content):
    with open('animals.html', 'w') as store_data:
        template_content_updated = store_data.write(content)

def main():
    animal_name = input("Enter a name of an animal:")
    data = data_fetcher.fetch_data(animal_name)

    output_replace = ''
    for animal in data:
        output_replace += serialize_animal(animal, animal_name)

    template_content = html_load()
    replaced_text = template_content.replace("__REPLACE_ANIMALS_INFO__", output_replace)
    html_store(replaced_text)

if __name__ == "__main__":
    main()