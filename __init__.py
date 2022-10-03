from mycroft import MycroftSkill, intent_file_handler


class WhisperAndAngry(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cough.side.head.intent')
    def handle_cough_side_head(self, message):
        self.speak_dialog('cough.side.head')


def create_skill():
    return WhisperAndAngry()

