
from typing import TypedDict, Dict , Any , List

class State(TypedDict):
    memory:Dict[str, Any]
    messgae_queue:Dict[str, Any]
    current_goal:str
    human_input:str
    agent_output:str
    step_number:int
    pre_string:str
    step_checklist:Dict[str,tuple[bool, Dict[str, Any]]]
    step_list:List[str]
    step_conversation:List[str, Any]
