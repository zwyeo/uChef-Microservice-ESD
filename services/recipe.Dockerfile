FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./recipe.py .
COPY ./themealdb-5744c-firebase-adminsdk-8izv6-23da3eb002.json .
CMD [ "python", "./recipe.py" ]
 
