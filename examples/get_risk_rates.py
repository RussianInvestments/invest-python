import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import RiskRatesRequest

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        request = RiskRatesRequest()
        request.instrument_id = ["BBG001M2SC01", "BBG004730N88"]
        r = client.instruments.get_risk_rates(request=request)
        for i in r.instrument_risk_rates:
            print(i.instrument_uid)
            print(i.short_risk_rate)
            print(i.long_risk_rate)


if __name__ == "__main__":
    main()
