from ovos_bus_client import MessageBusClient, Message

# Catching a message on the messagebus

print('Seeting up client to connect to a local OVOS instance')
client = MessageBusClient()

def print_utterance(message):
   print('OVOS said "{}"'.format(message.data.get('utterance')))\

print('Registering handler for speak message...')
client.on('speak', print_utterance)

client.run_forever()

# Sending a message on the bus

print('Setting up client to connect to a local OVOS instance')
client = MessageBusClient()
client.run_in_thread()

print('Sending speak message...')
client.emit(Message('speak', data={'utterance': 'Hello World'}))


# Catching a message on the messagebus

# print('Seeting up client to connect to a local OVOS instance')
# client = MessageBusClient()

# def print_utterance(message):
#     print('OVOS said "{}"'.format(message.data.get('utterance')))\

# print('Registering handler for speak message...')
# client.on('speak', print_utterance)

# client.run_forever()
