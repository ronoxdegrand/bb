class pad:
    def __init__(self, left, len):
        self.left = left
        self.len = len

    def mov(self, val):
        if val > 0 and self.left + self.len < 51:
            self.left += val
        if val < 0 and self.left > 0:
            self.left += val

    def inc(self, val):
        self.len += val
