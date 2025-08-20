import yagmail

class Message:


    def __init__(self, email, password):
        self.email = email
        self.yag = yagmail.SMTP(email, password)


    def sendEmail(self, addresess, photo, personID, confidence):
        for address in addresess:
            self.yag.send(address, "Person on your property!", [f"The person with ID {personID} is {confidence}% a person. Here’s an image attached."], photo)
            print(f"Email sent to: {address}") 
