import yaml

def get_countries(filename="countries.yaml"):
    """
    Get the countries in continents from countries.yaml
    """
    with open(filename, "r") as file:
        countries = yaml.load(file, Loader=yaml.FullLoader)
        return countries



