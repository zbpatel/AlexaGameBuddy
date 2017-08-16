# Game Buddy by Zac Patel 8/2017
# This skill is a rewrite of one of my first skills, Game Helper
# Since I wrote that skill, a few things have changed about the Alexa platform
# and I have learned a lot about how to better write for it.
# in addition, there were a variety of features that I did not get to add into
# Game Helper that I had planned on it, and I figured that I would be better
# able to do that through a rewrite.
# I am borrowing my "input santization" code from the previous version of this
# app because that took significant time to write and test, and without it the
# app would certainly fail Amazon's certification tests.
# Like the previous version of the app, some of the framework from this skill
# was taken from the very useful templates Amazon provides
# ------------------------------------------------------------------------------
# import for default (amazon) behavior
from __future__ import print_function

# here we import only the function handler methods to make the code more modular and easy to read
# each "handler" type method should take in only an intent, and return a completed response
from SpeechHelpers import build_speechlet_response, build_response
from RiskLogic import battle_handler, battle_probability_handler
from DiceLogic import roll_dice_handler

#from WordHelper import word_value_handler, word_checker_handler, word_spell_handle

# Code version number: (so it can be accessed from other files easily)
VERSION = "A"

# Event Handler Methods
def get_welcome_response():
    """
    Called if the user starts a session without specifying an intent
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "I can help with dice and Risk."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Can I help you with your game?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    """
    Called when the user tries to cancel or stop the current session
    """
    card_title = "Session Ended"
    speech_output = "Thank you for using Game Helper."

    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------
# Note to Self: These are the 4 different types of interactions that the user

def on_session_started(session_started_request, session):
    """ Called when the session starts (every time the skill is run)"""

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

# note, intent_request is event["request"] and session is event["session"]
def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # Pulling data from the JSON vector
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Selecting different behavior for different intent types
    if intent_name == "ROLLDICEINTENT":
        return roll_dice_handler(intent)
    elif intent_name == "SIMULATEBATTLEINTENT":
        return battle_handler(intent)
    elif intent_name == "CALCULATEPROBABILITYINTENT":
        return battle_probability_handler(intent)
    # Amazon's built in intent types below:
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------
# Note: this is the one that is specified during the online setup of the lambda function
def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    # Application ID added to prevent calls
    if (event['session']['application']['applicationId'] !=
             "ID here"):
         raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
