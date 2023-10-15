"""
CP1404 Practical 05
wimbledon.py

Write a program to read this file, process the data and display processed information.

the champions and how many times they have won.
the countries of the champions in alphabetical order

You need to store the data in appropriate data structures.
The solution uses: a list of lists, a dictionary and a set.

The file is not in simple ASCII format but UTF-8 with a byte order mark, or BOM.
You can account for this by setting the encoding like:

with open(filename, "r", encoding="utf-8-sig") as in_file:
For the final output of countries, use the join method to create a single string.

Use functions for each logical step/chunk of the program.
If you write it all in main to start with, that's fine, but then refactor it.
The solution uses 4 functions including main.

Sample output (truncated)
Wimbledon Champions:
Rod Laver 2
...
Lleyton Hewitt 1
Roger Federer 8
Rafael Nadal 2
Novak Djokovic 7
Andy Murray 2

These 12 countries have won Wimbledon:
AUS, CRO, ESP, FRG, GBR, GER, NED, SRB, SUI, SWE, TCH, USA

"""

CSV = "wimbledon.csv"


def main():
    """Read/process data and display result"""
    players = get_players()
    players.sort()
    print_players(players)
    countries = get_countries(players)
    print_countries(countries)


def get_players():
    """Read/process player data from file"""
    players = []
    with open(CSV, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])
            players.append(parts)
    return players


def print_players(players):
    """Print player data"""
    for player in players:
        print(f"{player[0]} ({player[3]}) - {player[2]}")
    print(f"\n{len(players)} players read from {CSV}")
    print(f"{len(get_countries(players))} countries")


def get_countries(players):
    """Get unique countries from players"""
    countries = set()
    for player in players:
        countries.add(player[3])
    return countries


def print_countries(countries):
    """Print countries"""
    countries = list(countries)
    countries.sort()
    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))


main()
