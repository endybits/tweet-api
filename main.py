from fastapi import FastAPI
from fastapi import status

app = FastAPI()

@app.get(
    path='/',
    status_code=status.HTTP_200_OK
)
async def home():
    return {
        'Twitter API': {
            'status': 'working'
        }
    }