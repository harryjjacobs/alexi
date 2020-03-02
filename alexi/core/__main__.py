from ..voice_assistant import VoiceAssistant

def main():
    assistant = VoiceAssistant()
    assistant.open()
    response = assistant.send_query('Definition of dancing')
    print(response)

if __name__ == "__main__":
    main()