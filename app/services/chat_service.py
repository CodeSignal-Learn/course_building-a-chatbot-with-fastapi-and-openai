import uuid
from openai import OpenAI
from models.chat import ChatManager

class ChatService:
    def __init__(self):
        self.chat_manager = ChatManager()
        self.openai_client = OpenAI()
        self.system_prompt = self.load_system_prompt('data/system_prompt.txt')
    
    def load_system_prompt(self, file_path: str) -> str:
        """Load the system prompt from file."""
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Error loading system prompt: {e}")
            return "You are a helpful assistant."
    
    def create_chat(self, user_id: str) -> str:
        """Create a new chat session."""
        chat_id = str(uuid.uuid4())
        self.chat_manager.create_chat(user_id, chat_id, self.system_prompt)
        return chat_id
    
    def process_message(self, user_id: str, chat_id: str, message: str) -> str:
        """Process a user message and get AI response."""
        chat = self.chat_manager.get_chat(user_id, chat_id)
        if not chat:
            raise ValueError("Chat not found")
        
        # Add user message
        self.chat_manager.add_message(user_id, chat_id, "user", message)
        
        try:
            # Get AI response
            conversation = self.chat_manager.get_conversation(user_id, chat_id)
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=conversation,
                temperature=0.7,
                max_tokens=500
            )
            
            ai_message = response.choices[0].message.content
            
            # Add AI response to chat history
            self.chat_manager.add_message(user_id, chat_id, "assistant", ai_message)
            
            return ai_message
            
        except Exception as e:
            raise RuntimeError(f"Error getting AI response: {str(e)}")