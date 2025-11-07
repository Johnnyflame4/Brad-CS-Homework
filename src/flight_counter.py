"""
Flight Counter 

A program that counts the number of flights for an airline given a file of flight data.

NAME: Brad Wing
SEMESTER: Fall 2025
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
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line and '::' in line:
                    code, name = line.split('::', 1)
                    airlines[code] = name
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        sys.exit(1)
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
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line and len(line) >= 2:
                    # Extract the first two characters as the airline code
                    airline_code = line[:2]
                    # Only count if this airline code exists in our airlines dictionary
                    if airline_code in airlines:
                        if airline_code in counters:
                            counters[airline_code] += 1
                        else:
                            counters[airline_code] = 1
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        sys.exit(1)
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
    if not counters:
        print("No flight data found.")
        return
    
    # Sort alphabetically by airline name
    sorted_airlines = sorted(counters.items(), key=lambda x: airlines.get(x[0], x[0]))
    
    # Calculate the total width for alignment
    total_width = 40
    
    for code, count in sorted_airlines:
        airline_name = airlines.get(code, code)
        # Format count with commas
        formatted_count = f"{count:,}"
        # Create the full line with proper spacing
        line = f"{airline_name}:{formatted_count:>{total_width - len(airline_name) - 1}}"
        print(line)

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
