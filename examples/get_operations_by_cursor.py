import os
from pprint import pprint

from tinkoff.invest import Client, GetOperationsByCursorRequest

token = os.environ["INVEST_TOKEN"]


with Client(token) as client:
    accounts = client.users.get_accounts()
    account_id = accounts.accounts[0].id

    def get_request(cursor=""):
        return GetOperationsByCursorRequest(
            account_id=account_id,
            instrument_id="BBG004730N88",
            cursor=cursor,
            limit=1,
        )

    operations = client.operations.get_operations_by_cursor(get_request())
    print(operations)
    depth = 10
    while operations.has_next and depth > 0:
        request = get_request(cursor=operations.next_cursor)
        operations = client.operations.get_operations_by_cursor(request)
        pprint(operations)
        depth -= 1
