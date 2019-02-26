#######
#NODES#
#######
class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after
