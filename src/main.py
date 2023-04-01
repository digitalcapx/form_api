from fastapi import FastAPI, HTTPException
from peewee import *
from models.form import Form, FormResponse
import logging, datetime

app = FastAPI()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', 
                    datefmt='%a, %d %b %Y %H:%M:%S', 
                    filename=f'src/logs/{datetime.date.today()}.log', 
                    filemode='a', encoding='utf-8')

@app.post("/form")
async def form(form_r: FormResponse):
    try:
        Form.create(name_surname=form_r.name_surname, email=form_r.email, phone=form_r.phone)
        logging.info(f"Formulário salvo com sucesso!")
    except Exception as e:
        logging.error(f"Não foi possível salvar o formulário.\nMESSAGE: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    return {"message":"Formulário salvo com sucesso!"}