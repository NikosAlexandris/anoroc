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
