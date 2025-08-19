import yagmail

class Message:


    def __init__(self, email, password):
        self.email = email
        self.yag = yagmail.SMTP(email, password)


    def sendEmail(self, addresess, photo):
        for address in addresess:
            self.yag.send(address, "Person on your property!", ["Here’s an image attached."], photo)
            print(f"Email sent to: {address}")
