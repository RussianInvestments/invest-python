class BaseService:
    _protobuf_stub = None

    def __init__(self, channel, metadata):
        self._stub = self._protobuf_stub(channel)
        self._metadata = metadata
