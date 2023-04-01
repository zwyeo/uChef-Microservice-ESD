FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./get_delivery_status.py ./amqp_setup.py ./firebase_setup.py ./fcm_cloud_messaging.py ./delivery_status_firebase.py ./serviceAccountKey.json ./
CMD [ "python", "./get_delivery_status.py" ]