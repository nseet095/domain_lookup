from sys import argv

from utils.utils import SearchTypes, print_help, get_search_types
from utils.searches import get_ssl_certificate

if __name__ == "__main__":
    # if len(argv) < 2:
    #     print_help()
    # if len(argv) > 2:
    #     search_types = get_search_types(argv[1:-2])
    # else:
    #     search_types = SearchTypes.ALL

    # print(search_types)

    certificate = get_ssl_certificate("google.com")
