from base_model import BaseModel
import peewee, pydantic


class Form(BaseModel):
    name_surname = peewee.CharField()
    email = peewee.CharField(unique=True)
    phone = peewee.CharField(unique=True)


class FormResponse(pydantic.BaseModel):
    name_surname: str
    email: str | None = None
    phone: str | None = None
    
    def to_form(self):
        form = Form()
        form.name_surname = self.name_surname
        form.email = self.email
        form.phone = self.phone
        return form
    

if __name__ == '__main__':
    try:
        Form.create_table()
        print("Tabela 'Form' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Form' ja existe!")