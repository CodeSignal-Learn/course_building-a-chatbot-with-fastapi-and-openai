class ChatManager:
    def __init__(self):
        self.chats = {}  # user_id -> chat_id -> chat_data
    
    def create_chat(self, user_id, chat_id, system_prompt):
        """Create a new chat for a user."""
        if user_id not in self.chats:
            self.chats[user_id] = {}
        
        self.chats[user_id][chat_id] = {
            'system_prompt': system_prompt,
            'messages': []
        }
    
    def get_chat(self, user_id, chat_id):
        """Get a chat by user_id and chat_id."""
        return self.chats.get(user_id, {}).get(chat_id)
    
    def add_message(self, user_id, chat_id, role, content):
        """Add a message to a chat."""
        if chat := self.get_chat(user_id, chat_id):
            chat['messages'].append({"role": role, "content": content})
    
    def get_conversation(self, user_id, chat_id):
        """Get the full conversation including system message."""
        if chat := self.get_chat(user_id, chat_id):
            return [
                {"role": "system", "content": chat['system_prompt']}
            ] + chat['messages']
        return []