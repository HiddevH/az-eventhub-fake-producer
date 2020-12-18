import os
from dotenv import load_dotenv
from faker_schema.faker_schema import FakerSchema
from faker_schema.schema_loader import load_json_from_file, load_json_from_string
from azure.eventhub import EventHubProducerClient, EventData

load_dotenv()

def send_fake_message(client, schema_file):
    """
    Generates a fake message and sends it to the EventHub
    """

    schema = load_json_from_file(schema_file)

    faker = FakerSchema()
    message = faker.generate_fake(schema)

    event_data_batch = client.create_batch()  # Create a batch of eventdata to send
    event_data_batch.add(EventData(message))

    client.send_batch(event_data_batch)

connection_str = os.getenv("EVENTHUB_CONNECTION_STR")
eventhub_name = os.getenv("EVENTHUB_NAME")
client = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)

schema_file = 'example_msg/hello.json'
msg_count = 10

i = 0
while i < msg_count:
    print(f'sending msg number {i}')
    i+=1
    send_fake_message(client, schema_file)

client.close()  # close connection before finishing