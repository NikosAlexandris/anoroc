#!/usr/bin/env python3
import wget
import pandas
import yaml


# load the data
data_confirmed = pandas.read_csv(filename1)
data_death = pandas.read_csv(filename2)
data_recovered = pandas.read_csv(filename3)

# Get the countries in continents from countries.yaml
with open("countries.yaml", "r") as file:
    countries = yaml.load(file, Loader=yaml.FullLoader)


def region(region_name, countries, data, exclude=[]):
    """ Makes a list of countries in the region.

    Parameters
    ----------
    region_name : string
        Choose one of the continents (e.g. "Asia") or "World".
    countries : dictionary
        List of countries under certain continent, from countries.yaml.
    data : numpy array
        All data loaded from the csv file.
    exclude: list
        List of countries you want to exclude.

    Returns
    -------
    region_name: string
        Region name. If some countries are excluded that is written in the name.
    region: list
        Returns the countries in the region.
    """

    continents = list(countries.keys()) + ["World"]

    if region_name not in continents:
        print(
            "Region name not valid. Choose from: \nAfrica, Asia, Europe, North America, Oceania, South America"
        )
        return None, None

    region = []

    # make the list of countries on certain continent or whole world
    for country in data["Country/Region"]:
        if region_name == "World":
            region.append(country)
        elif country in countries[region_name]:
            region.append(country)

    # deduplicate the list with multiple entries for the same country
    region = list(set(region))

    # remove excluded countries from the list
    if type(exclude) is str:
        exclude = [
            exclude,
        ]

    excluded = []
    for ex in exclude:
        if ex in region:
            excluded.append(ex)
            region.remove(ex)

    return region, excluded



if __name__ == "__main__":

    if args.country:
        country = args.country
        plot_countries([str(country)], title=country)
    elif args.region and args.exclude:
        region_name = args.region
        region, excluded = region(
            region_name, countries, data_confirmed, exclude=[str(args.exclude)]
        )
        if region and excluded:
            plot_countries(region, title=region_name + " excluding " + args.exclude)
        elif region:
            print(args.exclude + " not in " + args.region)
            print("Plotting data for the whole region.")
            plot_countries(region, title=region_name)
    elif args.region:
        region_name = args.region
        region, _ = region(region_name, countries, data_confirmed)
        if region:
            plot_countries(region, title=region_name)
    elif args.update:
        print("\n\nFresh data downloaded.")
    else:
        print("\nNo country selected. Plotting data for whole world.")
        world, _ = region("World", countries, data_confirmed)
        if world:
            plot_countries(world, title="World")
