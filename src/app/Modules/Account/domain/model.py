
from src.app.Modules.Account.domain.dto import AccountDTO
from src.app.Modules.Account.domain.interfaces import IAccount


class Account(IAccount):

    def __init__(self, dto: AccountDTO):
        self.load(dto)
        self.dto = dto

    def load(self, dto: AccountDTO):
        self.id = dto.id
        self.amount = dto.amount
        self.name = dto.name

    def get_amount(self):
        return self.amount

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name
