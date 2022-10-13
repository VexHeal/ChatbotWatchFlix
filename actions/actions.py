# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
# from rasa_core_sdk import Action
# from rasa_core_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "utter_add_movies"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         conn = sqlite3.connect("rasa.db")
#         c = conn.cursor()
#         c.execute("insert into movies(name,years) values('She:hulk', 2022)")
#         c.execute("insert into movies(name,years) values('007:No time to die', 2021)")
#         conn.commit()
#         dispatcher.utter_message(text="finish")
#
#         return []

class MoviesCheckList(Action):

    def name(self) -> Text:
        return "action_list"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect("E:/Anaconda/envs/py38_rasa/rasa0/actions/rasa.db")
        c = conn.cursor()

        movies_list = "select name from movies"
        c.execute(movies_list)
        conn.commit()

        result = [''.join(i) for i in c.fetchall()]
        strings = '\n'.join(result)

        dispatcher.utter_message(text=f"{strings}")

        return []

class MoviesSearch(Action):

    def name(self) -> Text:
        return "action_movies_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        coon = sqlite3.connect("E:/Anaconda/envs/py38_rasa/rasa0/actions/rasa.db")
        c = coon.cursor()

        Movies_name = tracker.get_slot("movies_name")

        movies_search = "select name from movies where name = ?"
        c.execute(movies_search, (Movies_name,))
        coon.commit()

        result = c.fetchone()

        if result == None:
            dispatcher.utter_message(text=f'sorry,\n it is not on Wtachflix')
        else:
            dispatcher.utter_message(text=f'{Movies_name} is on WtachFlix')

        return []