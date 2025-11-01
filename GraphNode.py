
from typing import Any, List, Tuple, Dict
from State import State
class GraphNode:


    def __init__(self,name:str, entrypoint:bool=False, db_connection:Any=None, state:State=None, start_index:int=None, should_summarize:bool=True):
        self.name=name
        self.entrypoint=entrypoint
        self.db_connection=db_connection
        self.incoming_edge=[]
        self.outgoing_edge=[]
        self.is_completed=False
        self.start_index=start_index
        self.should_summarize=should_summarize
        self.state=state
        self.step_data:Dict[str,Any]={}

    def add_incoming_edge(self,edge):
        self.incoming_edge.append(edge)
    
    def add_outgoing_edge(self,edge):
        self.outgoing_edge.append(edge)
    
    def get_incoming_edges(self):
        return self.incoming_edge
    
    def get_outgoing_edges(self):
        return self.outgoing_edge
    
    def get_name(self):
        return self.name

    def set_db_connection(self,db_connection:Any):
        self.db_connection=db_connection
    
    def get_db_connection(self):
        return self.db_connection
        

    def update_step_data(self, step_data:Dict[str,Any]):
        self.step_data.append(step_data)
    
    def set_is_completed(self,is_completed:bool, summary:str=None):
        self.is_completed=is_completed
        self.state['step_checklist'][self.name]=[is_completed, self.step_data]
        self.state['pre_string']=self.construct_pre_string(is_completed, summary)
        self.insert_memmory(summary)
    
    
    def set_state(self,state:State):
        self.state=state
    
    def get_state(self):
        return self.state

    def construct_pre_string(self,is_completed:bool, summary:str=None):
        if summary is None:
            return self.state['pre_string'] + f"Step {self.name}: is_completed={is_completed}"
        return self.state['pre_string'] + f"Step {self.name}: {summary}"
    
    def insert_memmory(self,summary:str):
        self.state['memory'][self.name]=summary

    
