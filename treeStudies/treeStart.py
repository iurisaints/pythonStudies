class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.key,
                                    self.key,
                                    self.right and self.right.key)