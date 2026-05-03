import datetime

class Email:
    def __init__(self, sender, receiver, subject, body, read = False, timestamp = None):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = read
        self.timestamp = datetime.datetime.now()
        
    def mark_as_read(self):
        self.read = True
        
    def display_email(self):
        self.mark_as_read()
        print("\n----- Email -----")
        print(f"From: {self.sender.name}")
        print(f"To : {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Body : {self.body}")
        print(f"Received: {self.timestamp.strftime("%Y-%m-%d %H:%M")}")
        print("------------------\n")
    
    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"[{status}] From : {self.sender.name} | Subject: {self.subject} | Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
        
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()
        
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver = receiver, subject = subject, body = body)
        receiver.inbox.receive_email(email)
        print(f'Email sent to {receiver.name} successfully.\n')
        
    def check_inbox(self):
        print(f"{self.name}'s Inbox:\n")
        self.inbox.list_email()
    
    def read_email(self, index):
        self.inbox.read_email(index)
    
    def delete_email(self, index):
        self.inbox.delete_email(index)

class Inbox():
    def __init__(self):
        self.emails = []
        
    def receive_email(self, email):
        self.emails.append(email)
    
    def list_email(self):
        if not self.emails:
            print("Inbox is empty.")
            return
        else:
            print("\n----- Inbox -----")
            for i, email in enumerate(self.emails, start = 1):
                print(f"{i}. {email}")
                print("------------------\n")
                
    def read_email(self, index):
        if not self.emails:
            print("Inbox is empty.")
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return
        self.emails[actual_index].display_email()
                
    def delete_email(self, index):
        if not self.emails:
            print("Inbox is empty.")
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return
        del self.emails[actual_index]
        print("Email deleted successfully.\n")
        
def main():
    tory = User("Tory")
    remy = User("Remy")
    
    tory.send_email(remy, "Hello", "Hi Remy, how are you?")
    remy.send_email(tory, "Re: Hello", "Hi Tory, I'm good! How about you?")
    
    remy.check_inbox()
    remy.read_email(1)
    remy.delete_email(1)
    remy.check_inbox()
    
    tory.check_inbox()
    tory.read_email(1)
    tory.check_inbox()
    
if __name__ == "__main__":
    main()      

