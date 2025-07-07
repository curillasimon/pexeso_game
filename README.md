# Dependencies

## Backend
python3 -m venv venv

Mac/Linux: source ./venv/bin/activate

Windows: .\venv\Scripts\activate

requirements.txt:

fastapi

uvicorn

pydantic

pip install -r requirements.txt

## Frontend

node.js REQUIRED

npm create vite@latest frontend --template react

cd frontend

npm install

npm install axios


git rm -r --cached venv

uvicorn pexeso_api:app --reload




