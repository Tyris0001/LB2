from datetime import datetime

class Invoice:
    def __init__(self, uid, price, status, gamepass, created):
        self.uid = uid
        self.price = price
        self.status = status
        self.gamepass = gamepass
        self.created = created

    def to_json(self):
        return {
            "uid": self.uid,
            "price": self.price,
            "status": self.status,
            "gamepass": self.gamepass,
            "created": self.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ')  # Serialize as string
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            uid=data["uid"],
            price=data["price"],
            status=data["status"],
            gamepass=data["gamepass"],
            created=datetime.strptime(data["created"], '%Y-%m-%dT%H:%M:%S.%fZ')  # Deserialize from string
        )

    def is_expired(self):
        return (datetime.now() - self.created).total_seconds() > 3600

    def get_uid(self):
        return self.uid

    def get_price(self):
        return self.price

    def get_status(self):
        return self.status

    def get_gamepass(self):
        return self.gamepass

    def get_created(self):
        return self.created

    def set_uid(self, uid):
        self.uid = uid

    def set_price(self, price):
        self.price = price
