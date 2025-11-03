"""
Flight Counter 

A program that counts the number of flights for an airline given a file of flight data.

NAME: <your name>
SEMESTER: <your semester>
"""
from typing import Dict
import argparse
import sys



def load_airlines(filename: str) -> Dict[str, str]:
    """Loads the airlines from the given file and returns a dictionary of airline codes and names.

    Example:
        >>> load_airlines("../data/airlines.dat")                    # doctest: +NORMALIZE_WHITESPACE
        {'UA': 'United Air Lines Inc.',
        'AA': 'American Airlines Inc.',
        'US': 'US Airways Inc.',
        'F9': 'Frontier Airlines Inc.',
        'B6': 'JetBlue Airways',
        'OO': 'Skywest Airlines Inc.',
        'AS': 'Alaska Airlines Inc.',
        'NK': 'Spirit Air Lines',
        'WN': 'Southwest Airlines Co.',
        'DL': 'Delta Air Lines Inc.',
        'EV': 'Atlantic Southeast Airlines',
        'HA': 'Hawaiian Airlines Inc.',
        'MQ': 'American Eagle Airlines Inc.',
        'VX': 'Virgin America'}

    Args:
        filename (str): The name of the file to load the airlines from.

    Returns:
        Dict[str, str]: A dictionary of airline codes and names.
    """
    airlines = {}
    return airlines


def build_counters(filename: str, airlines: Dict[str, str]) -> Dict[str, int]:
    """Builds a dictionary of airline counters from the given file.
       The file assumes the format of the airline code being
       the first two digits of the flight number, and each flight is on a unique line.


    Example:
        >>> build_counters("../data/flights10.dat", {"AA": "American Airlines",  \
                           "DL": "Delta Airlines", "UA": "United Airlines"})
        {'UA': 2, 'DL': 2}

    Args:
        filename (str): The name of the file to load the flights from.
        airlines (Dict[str, str]): A dictionary of airline codes and names.

    Returns:
        Dict[str, int]: A dictionary of airline counters.
    """
    counters = {}
    return counters


def print_counters(counters: Dict[str, int], airlines: Dict[str, str]) -> None:
    """Prints the counters in a formatted way.

    Example:
        >>> counters = {"AA": 10, "DL": 5, "UA": 3}
        >>> airlines = {"AA": "American Airlines", "DL": "Delta Airlines", "UA": "United Airlines"}
        >>> print_counters(counters, airlines)                   # doctest: +NORMALIZE_WHITESPACE
        American Airlines: 10
        Delta Airlines:     5
        United Airlines:    3


    Args:
        counters (Dict[str, int]): A dictionary of airline counters.
        airlines (Dict[str, str]): A dictionary of airline codes and names.
    """
    pass

def main(flights: str, airlines: str) -> None:
    """The main function of the program."""
    airlines_dict = load_airlines(airlines)
    counters = build_counters(flights, airlines_dict)
    print_counters(counters, airlines_dict)


# This program entry point uses the built in argparse module to parse command line arguments.
# You do not need to modify this code.
# to run the program using different type types of arguments, use the following commands:
# python flight_counter.py
# python flight_counter.py -f ../data/flights10.dat
# python flight_counter.py --flights ../data/flights10.dat
# You can also type python flight_counter.py -h to see the help message.
# these type of optional arguments are very common for command line programs
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flight Counter")
    parser.add_argument(
        "-f",
        "--flights",
        help="The file containing the flight data.",
        default="../data/flights10.dat",
    )
    parser.add_argument(
        "-a",
        "--airlines",
        help="The file containing the airline data.",
        default="../data/airlines.dat",
    )
    args = parser.parse_args()
    main(args.flights, args.airlines)
