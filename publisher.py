from google.cloud import pubsub_v1
import os

credentials_path = "./keys.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


publisher = pubsub_v1.PublisherClient()
topic_path = "projects/learning123gcp/topics/email-todo-logs"

def publish(data):
    publisher.publish(topic_path, data.encode("utf-8"))
