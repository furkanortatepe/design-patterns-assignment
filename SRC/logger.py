class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance
    def log(self, mesaj):
        self.logs.append(mesaj)
        print(f"[LOG] {mesaj}")
