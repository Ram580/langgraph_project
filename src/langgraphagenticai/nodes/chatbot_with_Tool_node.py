from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot with tool logic implementation.
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response with tool invocation.
        """
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])
        
        # Invoke the LLM with messages and tools
        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"
        
        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """
        Creates a chatbot instance with the configured model.
        
        Returns:
            ChatbotWithToolNode: An instance of the chatbot with tool integration.
            Returns a chatbot node function that can be used in a LangGraph workflow.
        """
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state: State) -> dict:
            """
            chatbot logic for processing the input state and generating a response. 
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
    
    
    