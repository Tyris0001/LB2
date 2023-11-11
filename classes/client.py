from datetime import timedelta

from classes.invoice import Invoice

class Client:
    def __init__(self, username, api_key, robux_earned, robux_balance, expires, plan, invoices, cookies):
        self.username = username
        self.api_key = api_key
        self.robux_earned = robux_earned
        self.robux_balance = robux_balance
        self.expires = expires
        self.plan = plan
        self.invoices = invoices
        self.cookies = cookies

    @classmethod # I LOVE FIRESHIP.IO!! 😢
    def from_json(cls, data):
        return cls(
            data.get("username"),
            data.get("api_key"),
            data.get("robux_earned"),
            data.get("robux_balance"),
            data.get("expires"),
            data.get("plan"),
            [Invoice.from_json(invoice_data) for invoice_data in data.get("invoices", [])],
            data.get("cookies")
        )

    def to_json(self):
        return {
            "username": self.username,
            "api_key": self.api_key,
            "robux_earned": self.robux_earned,
            "robux_balance": self.robux_balance,
            "expires": self.expires,
            "plan": self.plan,
            "invoices": [invoice.to_json() for invoice in self.invoices],
            "cookies": self.cookies
        }

    def set_invoices(self, invoices):
        self.invoices = invoices

    def get_invoices(self):
        return self.invoices

    def get_newest_invoice(self):
        return self.invoices[-1]

    def get_oldest_invoice(self):
        return self.invoices[0]

    def get_expored_invoices(self):
        return [invoice for invoice in self.invoices if invoice.is_expired()]

    def remove_expired_invoices(self, current_time):
        self.invoices = [invoice for invoice in self.invoices if
                         current_time - invoice.created <= timedelta(hours=1)]

    def add_invoice(self, invoice):
        self.invoices.append(invoice)