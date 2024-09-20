from pydantic import BaseModel


class UserSchema(BaseModel):
    fullname: str
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Kozhemyaka Artem Alexsandrovich",
                "email": "tvoyo_mblLo@mail.ru",
                "password": "password",
            }
        }


class UserLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {"email": "tvoyo_mblLo@mail.ru", "password": "password"}
        }
