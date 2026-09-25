#Social media application using abstraction
from abc import ABC, abstractmethod
class socialmedia(ABC):
    @abstractmethod
    def messanger(self):
        pass
    @abstractmethod
    def calls(self):
        pass
    @abstractmethod
    def search(self):
        pass
class whatsapp(socialmedia):  #Heirarchical inheritance
    def messanger(self):
        print("Whatsapp Messenger")
    def calls(self):
        print("Whatsapp Voice call")
    def search(self):
        print("Whatsapp Search")
    def status(self):
        print("Status Uploaded")
    def channels(self):
        print("Whatsapp Channel")
class Insta(socialmedia):  #Heirarchical inheritance
    def messanger(self):
        print("Insta Messenger")
    def calls(self):
        print("Insta Voice call")
    def search(self):
        print("Insta Search")
    def reels(self):
        print("Insta reels")
    def followers(self):
        print("Insta Followers")

what=whatsapp()
insta=Insta()

what.messanger()
what.calls()
what.channels()
print()
insta.messanger()
insta.search()
insta.reels()
insta.followers()