from .syft_message import SyftMessage


class GetObjectMessage(SyftMessage):
    def __init__(self, id):
        self.id = id
