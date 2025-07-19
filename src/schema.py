from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contrato de dados ou schema de dados ou view da minha API.
    name: str
    type: str

    class Config:
        orm_mode = True