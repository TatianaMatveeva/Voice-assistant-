registed_states = {}

def get_state(state_id):
    global root_state_id
    return registred_states[state_id]

def get_root_state[root_state_id]


class Transition:

    def __init__(self, to_id, synonims):
        self.to_id = to_id
        self.synonims = synonims
    
    def must_go(self, user_text):
        return user_text in self.synonims

    def get_desk_id(self):
        return self.to_id

class State:

    def __init__(self, id, text, transitions, default_transition, is_end = False):
        self.id = id
        self.text = text
        self.transitions = transitions
        self.default_transition = default_transition
        self.is_end = is_end

    def get_next_state(self, user_input):
        for transition in self.transitions:
            if transition.must_go(user_input):
                return get_state(transition.to_id)
            
        return get_state(self.default_transition)
    
    def register(self):
        global registed_states
        registed_states[self.id] = self
    
    def get_text():
        return self.get_text

    def get_id(self):
        return self.id
    
    def is_end_state(self):
        return self.is_end_state()

def init():
    global root_state_id
    State("100", "Привет! Вы хотите отправиться в космос?", [
        Transition()    
    ], None).register()

    State("900")
    root_state_id = "100"

init()
