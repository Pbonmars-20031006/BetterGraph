class HumanInputHandler:
    
    def __init__(self):
        pass
    
    def get_human_input(self) -> str:
        try:
            user_input = input("Enter your task/goal: ").strip()
            return user_input
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled by user")
            return ""

