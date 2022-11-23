from uuid import UUID
import json
from typing import Optional, List
from datetime import date, datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

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
        max_length=50,
        example='Endy'
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Bermudez'
    )
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

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

## Tweets

### Show all tweets
@app.get(
    path='/',
    #response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets']
)
async def home():
    return {
        'Twitter API': {
            'status': 'working'
        }
    }

### Create a tweet
@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a Tweet',
    tags=['Tweets']
)
async def post_tweet():
    pass

### Show a tweet
@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a tweet',
    tags=['Tweets']
)
async def show_a_tweet():
    pass

### Update a tweet
@app.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
async def update_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
async def delete_a_tweet():
    pass


## Users

### Registe a user
@app.post(
    path='/users',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User',
    tags=['Users']
)
async def signup(
    user: UserRegister = Body(...)
):
    """
        Signup a user

        This path operation register a user in the app.
        
        Parameters:
        - Request body parameter
            - user: UserRegister
        
        Returns a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open('users.json', 'r+', encoding='utf-8') as f:
        results = f.read()
        results = json.loads(results)
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict.get('user_id'))
        user_dict['birth_date'] = str(user_dict.get('birth_date'))
        results.append(user_dict)
        results = json.dumps(results)
        f.seek(0)
        f.write(results)
        return user

### Login a user
@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=['Users']
)
async def login():
    pass

### Show all users
@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users']
)
async def show_all_users():
    """
        Show all users

        This path operation show all users registered in users.json
        
        Parameters: None
        
        Returns a json list with the basic user information for each item:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    with open('users.json', 'r', encoding='utf-8') as f:
        results = f.read()
        results = json.loads(results)
    return results

### Show user detail
@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a User',
    tags=['Users']
)
async def show_user_detail():
    pass

### Update a user
@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a User',
    tags=['Users']
)
async def update_an_user():
    pass

### Delete a user
@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a User',
    tags=['Users']
)
async def delete_an_user():
    pass