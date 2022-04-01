import pulsar

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')

# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer('topic-input')
# Send a message to consumer
sentence = 'Welcome to Data Engineering Course! Hello from Lingkai in the Producer node!'
words = sentence.split()
for word in words:
    producer.send(word.encode('utf-8'))
producer.send(("END SESSION!").encode('utf-8'))
# Destroy pulsar client
client.close()

