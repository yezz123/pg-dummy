import argparse


def parseargs():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A Script Help to Populate a PostgreSQL Database with Dummy Data",
    )
    parser.add_argument(
        "-d",
        "--database",
        dest="database",
        default="postgres",
        type=str,
        help="The database with which you wish to connect",
    )
    parser.add_argument(
        "-n",
        "--hostname",
        dest="hostname",
        default="127.0.0.1",
        type=str,
        help="The hostname or IP of the postgresql database",
    )
    parser.add_argument(
        "-l",
        "--length",
        dest="length",
        default="1",
        type=int,
        help=" The length you want the dummy inserter to run",
    )
    parser.add_argument(
        "-p",
        "--password",
        dest="password",
        default="postgres",
        type=str,
        help="The password of the connection user",
    )
    parser.add_argument(
        "-t",
        "--table",
        dest="table",
        default="data",
        type=str,
        help=" The database table onto which you wish to write data",
    )
    parser.add_argument(
        "-u",
        "--user",
        dest="user",
        default="postgres",
        type=str,
        help="The user with which to connect",
    )
    return parser.parse_args()
