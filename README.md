# AZ Eventhub Fake Producer
<img src="logo.png" width="500">
Send over fake messages over to the EventHub using a pre-defined schema.

As an example, main.py imports the schema:
`from message_schema.example import fake_message  # Import randomly generated message`

You can also define your own schema using the example's logic and the Joke2k's faker providers at https://faker.readthedocs.io/en/stable/

## How to:
create dotenv variables for:
`EVENTHUB_CONNECTION_STR`

`EVENTHUB_NAME`

set `num_of_messages` to desired fake message count to send to EventHub

Run main.py


Dependent on Joke2k's faker: https://github.com/joke2k/faker
