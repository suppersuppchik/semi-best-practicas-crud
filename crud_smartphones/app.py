import fastapi
from pydantic_settings import BaseSettings
import db
import crud
import schemas


class Settings(BaseSettings):
    connection_string: str


settings = Settings()
app = fastapi.FastAPI()


db = db.get_database(settings.connection_string)


@app.get('/all', response_model=list[schemas.GetSmartphone])
async def all_smartphones():
    return crud.get_smartphones(db)


@app.post('/create-smartphone', response_model=schemas.CreateSmartphone)
async def create_smartphone(smartphone: schemas.CreateSmartphone):
    return crud.add_smartphone(db=db, smartphone=smartphone)


@app.put('/update-smartphone/{smartphone_id}', response_model=schemas.UpdateSmartphone)
async def update_smartphone(smartphone_id: str, smartphone: schemas.UpdateSmartphone):
    return crud.update_smartphone(db=db, smartphone=smartphone, smartphone_id=smartphone_id)


@app.delete('/delete-smartphone/{smartphone_id}', response_model=schemas.DeleteSmartphone)
async def delete_smartphone(smartphone_id: str):
    return crud.delete_smartphone(db, smartphone_id)
