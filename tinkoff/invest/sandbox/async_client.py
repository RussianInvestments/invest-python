from tinkoff.invest import AsyncClient
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX


class AsyncSandboxClient(AsyncClient):
    def __init__(
        self,
        token: str,
        **kwargs,
    ):
        kwargs["target"] = INVEST_GRPC_API_SANDBOX
        super().__init__(token, **kwargs)
