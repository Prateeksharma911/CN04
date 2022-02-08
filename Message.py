
class printMessage:
    def __init__(self,element , command):
        self.element = element 
        self.command = command

    def getMessage(self):

        if self.element=="frog":
            return f"I’m {self.element}! I am {self.command} today"
            
        else:
            return f"i'm {self.element}! I'm sometimes {self.command}"
