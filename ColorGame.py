import Message as Message


class ColorGame:

    # Colour codes
    def __init__(self):
        self.subscriber = {
            "banana":False,
            "ink":False,
            "salt":False,
            "frog":False,
            "blood":False,
            "sky":False,
            "apple":False}
            
        self.color = {
            "red":["ink","blood","apple"],
            "black":["ink","sky"],
            "yellow":["banana","frog"],
            "green":["apple","banana"],
            "blue":["sky","frog"],
            "white":["salt"]
        }
        
    def ListAll(self):
        elements=[]
        for element in self.subscriber:
            if self.subscriber[element]:
                elements.append(element)

        return elements
    

    def subscribe_unsubscribe(self,element , value):

        if self.subscriber[element]==value==True:
            return "already subscribed"

        elif self.subscriber[element]==value==False:
            return "already Unsubscribed"

        self.subscriber[element] = value

        if value:
            return f"subscribing {element}"

        else:
            return f"unsubscribing {element}"
    
    def printColor(self,command):

        outputColors = []

        for element in self.color[command]:
            if self.subscriber[element]:
                outputColors.append(Message.printMessage(element,command).getMessage())

        return outputColors
    
    def evalInput(self,command):

        if type(command)==str:

            if command=="list":
                return str(self.ListAll())

            if command[0]=="+" and command[1:] in self.subscriber:
                return self.subscribe_unsubscribe(command[1:],True)

            elif command[0]=="-" and command[1:] in self.subscriber:
                return self.subscribe_unsubscribe(command[1:],False)

            elif command[0]=="+" or command[0]=="-":
                return "Invalid Thing Name"

            elif command in self.color:
                return self.printColor(command)

            else:
                return ""

        else:

            return ""

