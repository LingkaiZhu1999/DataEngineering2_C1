import pulsar

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to a topic and subscription
consumer = client.subscribe('topic-output', subscription_name='DE-sub')
State = True
sentence = ''
while State:
    msg = consumer.receive()
    try:
        word = msg.data().decode('utf-8')
        if word == "END SESSION!":
            State = False
            consumer.acknowledge(msg)
        else:
            sentence += word + ' '  # data merging
            consumer.acknowledge(msg)
    except:
        consumer.negative_acknowledge(msg)
print(sentence)

# Destroy pulsar client
client.close()
