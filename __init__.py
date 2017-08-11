


import requests
from requests.auth import HTTPDigestAuth
import json
import datetime
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill

__author__ = 'Ramkumar Reddi'


# TODO - Localization
class MedicationSkill(MycroftSkill):
    def __init__(self):
        super(MedicationSkill, self).__init__("MedicationSkill")

    def initialize(self):
        intent = IntentBuilder("MedicationIntent").require("QueryKeyword") \
            .require("Medication").build()
        self.register_intent(intent, self.handle_intent)


    def handle_intent(self, message):

        # Replace with the correct URL
        url = "http://10.1.1.60:8080/Thingworx/Things/medication_thing/Properties"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            #'Content-Type: 'application/json',
            'appKey':'5cc163c6-e9e6-44c6-9ae6-6a42f4ac9532'
            }
        try:
            
            myResponse = requests.get(url,headers=headers)
            if(myResponse.ok):

                # Loading the response data into a dict variable
                # json.loads takes in only binary or string variables so using content to fetch binary content
                # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
                x = json.loads(myResponse.content.decode('utf-8'))
                Medication = x['rows'][0]['Force']
                print("\n")
               # print (x['rows'][0]['Diastolic'])
                self.speak_dialog("Medication", {"Medication": Medication})
            else:
                return
        except:
            return none

    def stop(self):
        pass


def create_skill():
    return MedicationSkill()
