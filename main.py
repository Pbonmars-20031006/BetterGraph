from typing import List
from GraphNode import GraphNode
from HumanInputHandler import HumanInputHandler
from AgentOutputHandler import AgentOutputHandler
from State import State






def insert_steps(step_list:List[str]):
    step_nodes=[]
    for idx, step in enumerate(step_list):
        if idx==0:
            stepnode=GraphNode(name=step,entryPoint=True. should_summarize=True)
            step_nodes.append(stepnode)
        else:
            stepnode=GraphNode(name=step, should_summarize=True)
            stepnode.outgoing_edge.append(step_nodes[-1])
            step_nodes.append(stepnode)
    return step_nodes


def main():

    
    Human_Input_Handler=HumanInputHandler()
    Agent_Output_Handler=AgentOutputHandler()
    Formatting=Formatting()
    human_input=HumanInputHandler().get_human_input()
    pre_string=f"{human_input}\nSteps have been generated, please follow the steps to complete the task."
    format_human_input=Formatting.format_user_string(human_input)
    step_list=Agent_Output_Handler.get_step_list(format_human_input, style="step_generator" , model_id="claude-3-5-sonnet-20240620", invocation_config={"max_tokens":1000}) #invoke model to generate step list
    step_nodes=insert_steps(step_list)
    
    state=State(memory={}, messgae_queue=[format_human_input], current_goal="", human_input=human_input, agent_output="", step_number=0, pre_string=pre_string, step_checklist={}, step_list=step_list, step_conversation=[])


    for idx, step_node in enumerate(step_nodes):
        step_node.set_state(state)
        pre_string=state['pre_string'] + "Goal: " + step_node.get_name()
        format_pre_string=Formatting.format_user_string(pre_string)
        step_conversation=[]
        step_conversation.append(format_pre_string)
        while True:
            agent_output=Agent_Output_Handler.get_agent_output(step_conversation , model_id="claude-3-5-sonnet-20240620", style="conversation", invocation_config={"max_tokens":1000})
            if agent_output.check_if_completed():
                summary=Agent_Output_Handler.get_summary(step_conversation, style="summary", model_id="claude-3-5-sonnet-20240620", invocation_config={"max_tokens":500})
                step_node.insert_memmory(summary)
                step_node.set_is_completed(True, summary)
                state['memory'].update({step_node.get_name(): summary})
                break
            else:
                result=Agent_Output_Handler.handle_tool_call(agent_output)
                result=Formatting.format_user_string(result)
                step_conversation.append(agent_output)
                step_conversation.append(result)
                state['messgae_queue'].append(agent_output)
                state['messgae_queue'].append(result)
            
        
                