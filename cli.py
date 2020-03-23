import argparse
import os
from .constants import URL_CONFIRMED
from .constants import URL_DEATH
from .constants import URL_RECOVERED
from .constants import FILENAME1
from .constants import FILENAME2
from .constants import FILENAME3


prog_descrip = """Pull csv corona data from github repo. Plot country cases."""

parser = argparse.ArgumentParser(description=prog_descrip)
parser.add_argument(
    "-u", "--update", action="store_true", help="Download and update the csv file."
)

parser.add_argument(
    "-c", "--country", help="Input name of the country which you want to plot."
)

parser.add_argument(
    "-r",
    "--region",
    help="Input name of the region which you want to plot. You can choose from Africa, Asia, Europe, North America, Oceania, South America.",
)

parser.add_argument(
    "-e",
    "--exclude",
    help="Input name of the country which you want to be excluded from the region.",
)

args = parser.parse_args()

# update the csv data if the update flag is passed
if args.update:
    if os.path.exists(filename1):
        os.remove(filename1)
    if os.path.exists(filename2):
        os.remove(filename2)
    if os.path.exists(filename3):
        os.remove(filename3)

# download csv if file doesn't exist
if not os.path.exists(filename1):
    print("\n\nDownloading data.")
    wget.download(url_confirmed, out=filename1)
if not os.path.exists(filename2):
    wget.download(url_death, out=filename2)
if not os.path.exists(filename3):
    wget.download(url_recovered, out=filename3)
