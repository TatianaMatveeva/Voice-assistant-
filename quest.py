registed_states = {}

class Transition:

    def __init__(self, to_id, synonims):
        self.to_id = to_id
        self.synonims = synonims
    
    def must_go(self, user_text):
        return user_text in self.synonims

    def get_desk_id(self):
        return self.to_id

class State:

    def __init__(self, id, text, transitions, default_transition):
        self.id = id
        self.text = text
        self.transitions = transitions
        self.default_transition = default_transition

    def get_next_state(self, user_input):
        for transition in self.transitions:
            if transition.must_go(user_input):
                return get_state(transition.to_id)
            
        return get_state(self.default_transition)
    
    def register(self):
        global registed_states
        registed_states[self.id] = self

            
def init():
    global root_state_id
    State("100", "Привет! Вы хотите отправиться в космос?", []).register()

    root_state_id = "100"

