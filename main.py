import os
import time
from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData
from message_schema.example import fake_message  # Import randomly generated message

num_of_messages = 10

def send_message(client, message):
    """Send a message to the EventHub.

    Keyword arguments:
    client -- the eventhub client
    message -- the message to send
    """
    event_data_batch = client.create_batch()  # Create a batch of eventdata to send
    event_data_batch.add(EventData(message))  # Add message to the batch
    client.send_batch(event_data_batch)  # Send the batch

def generate_fake_messages(client, msg_count):
    """Generates a given number of messages and sends them to the EventHub.

    Keyword arguments:
    client -- the eventhub client
    msg_count -- number of messages to generate
    """
    # Set number of messages to send

    i = 0  # initiate counter
    while i < msg_count:
        print(f'sending msg number {i}')
        i+=1
        send_message(client, fake_message())  # send a fake message to eventhub
        time.sleep(0.5) # wait for 0.5s to produce next message for fun

# Import EventHub connection info embedded in environmental variables
load_dotenv()

# Set connection str variables
connection_str = os.getenv("EVENTHUB_CONNECTION_STR")
eventhub_name = os.getenv("EVENTHUB_NAME")
client = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)

generate_fake_messages(client, msg_count=num_of_messages)  # generate messages and send them to the eventhub

client.close()  # close connection to end session