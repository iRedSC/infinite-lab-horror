class Path:
    """
    Initialize a path by creating a new instance and giving it a namespace.
    >>> path = Path("testing")

    Then call the function with a string that will be the file's name.
    >>> path("main")

    "testing:main"
    """

    def __init__(self, namespace):
        self.namespace = namespace

    def __call__(self, path):
        return f"{self.namespace}:.{path}"
