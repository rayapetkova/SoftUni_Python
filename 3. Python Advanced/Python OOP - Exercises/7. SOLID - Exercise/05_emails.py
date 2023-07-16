from abc import ABC, abstractmethod


class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def sender_format(self):
        pass


class IReceiver(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def receiver_format(self):
        pass


class IContent(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def content_format(self):
        pass


class MyMl(ISender, IReceiver, IContent):
    def __init__(self, sender, receiver, content):
        super().__init__(sender)
        self.receiver = receiver
        self.content = content

    def sender_format(self):
        return ''.join(["I'm ", self.sender])

    def receiver_format(self):
        return ''.join(["I'm ", self.receiver])

    def content_format(self):
        return '\n'.join(['<myML>', self.content, '</myML>'])


class HTML(ISender, IReceiver, IContent):
    def __init__(self, sender, receiver, content):
        super().__init__(sender)
        self.receiver = receiver
        self.content = content

    def sender_format(self):
        return ''.join(["I'm ", self.sender])

    def receiver_format(self):
        return ''.join(["I'm ", self.receiver])

    def content_format(self):
        return '\n'.join(['<html>', self.content, '</html>'])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.sender_format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.receiver_format()

    def set_content(self, content):
        self.__content = content.content_format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


# Test code:

myml = MyMl('Random sender', 'Random receiver', 'Hello!')
email = Email('IM')
email.set_sender(myml)
email.set_receiver(myml)
email.set_content(myml)
print(email)
