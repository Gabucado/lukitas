from src.app.Modules.Debt.domain.dto import DebtDTO
from src.app.Modules.Debt.domain.interfaces import IDebt


class Debt(IDebt):
    def __init__(self, dto: DebtDTO) -> None:
        self.dto = dto
        self.load(dto)

    def load(self, dto):
        self.id = dto.id
        self.name = dto.name
        self.currency = dto.currency
        self.date = dto.date
        self.amount = dto.amount
        self.debtor = dto.debtor
        self.creditor = dto.creditor

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_currency(self):
        return self.currency

    def get_date(self):
        return self.date

    def get_amount(self):
        return self.amount

    def get_debtor(self):
        return self.debtor

    def get_creditor(self):
        return self.creditor
