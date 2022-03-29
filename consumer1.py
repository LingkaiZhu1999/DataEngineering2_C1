import pulsar

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to a topic and subscription
consumer = client.subscribe('topic-output', subscription_name='DE-sub')
State = True
sentence = ''
i = 12
while State:
    msg = consumer.receive()
    try:
        word = msg.data().decode('utf-8')
        sentence += word + ' '
        consumer.acknowledge(msg)
        i -= 1
        if i == 0:
            State = False
    except:
        consumer.negative_acknowledge(msg)
print(sentence)

# Destroy pulsar client
client.close()
