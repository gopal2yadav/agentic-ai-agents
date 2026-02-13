class Memory:
    """Simple in-memory storage for agent conversations and context."""

    def __init__(self):
        self.storage = []

    def add(self, message):
        """Add a message or event to the memory."""
        self.storage.append(message)

    def get_context(self, limit=None):
        """Retrieve the last `limit` messages from memory; if limit is None, return all."""
        if limit is None or limit >= len(self.storage):
            return self.storage
        return self.storage[-limit:]
