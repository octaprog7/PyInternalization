import sys
import os
import pathlib
from src.internaliztn.internationalization import CSVProvider, SQLiteDataProvider

if __name__ == '__main__':
    fn = "translated.csv"
    pth = pathlib.Path(sys.argv[0]).parent
    db_fn = f"{pth}{os.path.sep}{fn}"
    print("CSV Provider:")
    provider = CSVProvider(db_fn, "strID", "RU")
    #
    print(f"len: {len(provider)}")
    print(f"Epilog: {provider('strEpilog')}")

    fn = "strings.db3"
    db_fn = f"{pth}{os.path.sep}{fn}"
    print("SQLite Provider:")
    provider = SQLiteDataProvider(fn, "str_id", "FR")
    print(f"len: {len(provider)}")
    print(f"strSecond: {provider('strSecond')}")
