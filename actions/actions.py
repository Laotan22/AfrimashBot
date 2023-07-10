# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from googletrans import Translator

translator = Translator()

def translate(statement):
    # timeout = 0
    # while Exception:  # and timeout < 5:
    try:
        name = (translator.translate(statement, dest='yo'))
        return name.text
        # break

    except Exception as e:
         return name.text


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_translate_text"

    #
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # destination_language = next(tracker.get_latest_entity_values("language"), None)

        bot_event = next(e for e in reversed(tracker.events) if e["event"] == "bot")

        dispatcher.utter_message(text=translator.translate(bot_event.text))

        return []



        # except AttributeError:
#   print("Error")
