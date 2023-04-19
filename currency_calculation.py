import requests, json
from argparse import ArgumentParser

"""
    https://exchangeratesapi.io/
    -f USD
    -t TRY
    -a 40
    python3 config.py -f EUR -t TRY -a 123
"""

API_KEY = "32XN0MLAatdRWYfVE3M4BlAkCUczVd0l"


def main():
    parser_ = arg_parser()

    to_ = parser_.to_.upper()
    from_ = parser_.from_.upper()
    amount_ = parser_.amount_

    print_result(to_, from_, amount_)


def print_result(to_, from_, amount_):
    if len(to_) != 3 or len(from_) != 3:
        raise ValueError("Please enter a valid currency code")
    else:
        result = api(to_, from_, amount_)
        print(f"Result: {from_} => {to_}", result)


def api(to_, from_, amount_):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount_}"
    headers = {"apikey": API_KEY}
    response = requests.request("GET", url, headers=headers).json()
    return response["result"]


def arg_parser():
    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        "-t",
        "--to_",
        required=False,
        help="To currency, default is 'TRY'",
        type=str,
        default="TRY",
    )
    arg_parser.add_argument(
        "-f",
        "--from_",
        required=False,
        help='From currency, default is "USD"',
        type=str,
        default="USD",
    )
    arg_parser.add_argument(
        "-a", "--amount_", required=True, help="From currency, default is 1", type=int
    )

    return arg_parser.parse_args()


main()
