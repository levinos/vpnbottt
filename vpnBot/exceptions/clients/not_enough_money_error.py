from vpnBot.exceptions.clients.client_base_error import ClientBaseError
from vpnBot.static.texts_storage import TextsStorage


class NotEnoughMoneyError(ClientBaseError):
    def __init__(self, message: str = TextsStorage.NOT_ENOUGH_MONEY_ERROR_MSG) -> None:
        self.message = message
        super().__init__(message)
