from src.app.Modules.Transaction.domain.dto import TransactionDTO


class Transaction:
    def __init__(self, dto: TransactionDTO):
        self.dto = dto
        self.load(dto)

    def load(self, dto:TransactionDTO):
        self.id = dto.id
        self.name = dto.name
        self.paymentMethod = dto.paymentMethod
        self.amount = dto.amount
        self.currency = dto.currency
        self.origin = dto.origin
        self.destiny = dto.destiny
        self.category = dto.category

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_paymentMethod(self):
        return self.paymentMethod

    def get_amount(self):
        return self.amount

    def get_currency(self):
        return self.currency

    def get_origin(self):
        return self.origin

    def get_destiny(self):
        return self.destiny

    def get_category(self):
        return self.category
