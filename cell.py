class cell:
    def __init__(self):
        ## not sure what this does so excluding
        # super(cell, self).__init__()
        ## just for now
        self.isalive = 0 # Default to being dead

    def die(self):
            self.isalive = 0

    def live(self):
            self.isalive = 1
