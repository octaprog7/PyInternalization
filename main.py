import sys
from src.internaliztn.internationalization import CSVProvider

if __name__ == '__main__':
    fn = sys.argv[1]
    provider = CSVProvider(fn, "strID", "RU")
    #
    print(f"len: {len(provider)}")
    print(f"Epilog: {provider('strEpilog')}")
