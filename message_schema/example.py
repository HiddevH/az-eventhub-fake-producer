from faker import Faker

def fake_message():
    fake = Faker()
    message = {
        'id': fake.uuid4(),
        'name' : fake.name(),
        'result': fake.random_element(elements=('R', 'A', 'B', 'C')),
        'bank_number': fake.bban(),
        'statedIp': fake.ipv4()
    }
    return message