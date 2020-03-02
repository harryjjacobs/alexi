import logging
from mycroft_bus_client import MessageBusClient, Message

LOG = logging.getLogger(__name__)

class VoiceAssistant():
    def __init__(self):
        LOG.info("Setting up client to connect to a local mycroft instance")
        self.client = MessageBusClient()

    def open(self):
        self.client.run_in_thread()

    def close(self):
        self.client.close()

    def send_query(self, query):
        message = Message("recognizer_loop:utterance", {'utterances': [query.strip()]})
        response = self.client.wait_for_response(message, 'speak', timeout=20.0)
        if response is not None:
            return response.data['utterance']