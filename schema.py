from pydantic import BaseModel, EmailStr
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'username': "jyotixzy",
                'email': 'kumari008jyoti@gmail.com',
                'password': '99999',
                'is_staff': False,
                'is_active': True
            }
        }
class Settings(BaseModel):
    authjwt_secret_key:str='fa30de26ea0ff708ef1aaf69dd6e55d278a522b74f765ff21d34b8bea97eda7c'

class LoginModel(BaseModel):
    username:str
    password:str

class OrderModel(BaseModel):
    id :Optional[int]
    quantity: int
    order_status:Optional[str]='PENDING'
    pizza_size:Optional[str]='SMALL'
    user_id:Optional[int]
    class Config:
        orm_mode = True 
        schema_extra={
            'example':{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }