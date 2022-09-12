




class Path:
    def __init__(self, namespace):
        self.namespace = namespace

    def __call__(self, path):
        return f"{self.namespace}:{path}"