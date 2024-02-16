from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    first_name: str
    last_name: str
    email_address: EmailStr
    phone_number: str
    password: str
