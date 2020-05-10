import win32com.client
import win32com

class CustomOutlook():
    def __init__(self):
        self.msg = ''
        self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        self.inbox = self.outlook.GetDefaultFolder(6)
    
    def __del__(self):
        print("Finished Succesfully")
    
    def read_email_from_outlook(self):    
        messages = self.inbox.Items
        '''message = messages.GetLast()
        body_content = message.Body
        subject = message.Subject
        categories = message.Categories
        print(body_content)
        print(subject)
        print(categories)'''

        for message in messages:
            if message.UnRead:
                print(message.Subject)