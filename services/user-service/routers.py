from fastapi import APIRouter
router = APIRouter()

@router.post('/user',response_model=dict)
def create_user(user:dict):
    return {"username": "vlad123", "password": "asd123asd"}


