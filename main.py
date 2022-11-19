from uuid import UUID
from typing import Optional, List
from datetime import date, datetime
# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_day: Optional[date] = Field(default=None)


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(
        default=datetime.now()
    )
    updated_at: Optional[datetime] = Field(default=None)
    owner: User = Field(...)

# Path Operations
@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    tags='Home'
)
async def home():
    return {
        'Twitter API': {
            'status': 'working'
        }
    }

## Users
@app.post(
    path='/users',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User',
    tags=['Users']
)
async def signup():
    pass


@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=['Users']
)
async def login():
    pass


@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users']
)
async def show_all_users():
    pass


@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a User',
    tags=['Users']
)
async def show_user_detail():
    pass


@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a User',
    tags=['Users']
)
async def update_an_user():
    pass


@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a User',
    tags=['Users']
)
async def delete_an_user():
    pass



## Tweets