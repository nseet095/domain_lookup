from enum import Enum


class SearchTypes(Enum):
    ALL = 1
    CERT = 2
    IP = 3
    REVERSE_IP = 4
    TLD = 5


# Check if ip belongs to vpn provider in ip check


def print_help() -> None:
    print("This utility searches ")


def get_search_types(argv: list[str]) -> list[SearchTypes]:
    modes = []
    if "-a" in argv:
        return [SearchTypes.ALL]
    if "-c" in argv or "--cert" in argv:
        modes.append(SearchTypes.CERT)
    if "-i" in argv or "--ip" in argv:
        modes.append(SearchTypes.IP)
    if "-r" in argv or "--rip" in argv:
        modes.append(SearchTypes.REVERSE_IP)
    if "-t" in argv or "--tld" in argv:
        modes.append(SearchTypes.TLD)
    return modes
