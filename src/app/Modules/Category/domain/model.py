from src.app.Modules.Category.domain.dto import CategoryDTO
from src.app.Modules.Category.domain.interfaces import ICategory


class Category(ICategory):
    def __init__(self, dto: CategoryDTO):
        self.dto = dto
        self.load(dto)

    def load(self, dto: CategoryDTO):
        self.id = dto.id
        self.name = dto.name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
