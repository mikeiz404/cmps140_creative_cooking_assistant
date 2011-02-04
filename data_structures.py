"""
Data structures used for communication between modules.
"""

class ConversationState(object):
    """
    Stores all state associated with a conversation.  Instances are
    created when a conversation begins and are passed throughout the
    application.  The receiver of a ConversationState will update the
    state by modifying the ConversationState that it receives.

    The ConversationState can be persisted by pickling it using the
    pickle or cPickle modules.
    """

    def __init__(self):
        self.user_name = ""
        self.last_user_input = ""
        self.current_state = "greeting"


class Message(object):
    """
    Base class for messages exchanged between the NLU and DM and DM
    and NLG.  It implements frame-and-slot semantics through its
    frame attribute, which is a dictionary.  It also stores metadata
    using its other attributes.
    """

    def __init__(self):
        """
        Create a new Message.
        """
        self.mood = None # Or some sensible default.
        self.frame = {}


class ParsedInputMessage(Message):
    """
    Parsed representation of user input, generated by the NLU for use
    by the DM.
    """

    def __init__(self, raw_input_string):
        """
        Create a new ParsedInput.
        """
        Message.__init__(self)
        self.raw_input_string = raw_input_string

    """
    Fills out the message meta and frame attributes.
    """
    def parse(self):
        pass
        
    """
    Returns a confidence value for the raw_input_string matching the
    message type.
    """
    def confidence(self):
        return 0.0

class ContentPlanMessage(Message):
    """
    Representation of content to express to user, generated by the DM
    for use by the NLG.
    """

    def __init__(self, description):
        Message.__init__(self)
        self.description = description
        
