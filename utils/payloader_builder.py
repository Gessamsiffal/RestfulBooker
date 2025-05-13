class BookingPayloadBuilder:
    def __init__(self):
        self.payload = {}

    def set_firstname(self, name):
        self.payload["firstname"] = name
        return self

    def set_lastname(self, name):
        self.payload["lastname"] = name
        return self

    def set_totalprice(self, price):
        self.payload["totalprice"] = price
        return self

    def set_depositpaid(self, paid):
        self.payload["depositpaid"] = paid
        return self

    def set_checkin(self, checkin_date):
        if "bookingdates" not in self.payload:
            self.payload["bookingdates"] = {}
        self.payload["bookingdates"]["checkin"] = checkin_date
        return self

    def set_checkout(self, checkout_date):
        if "bookingdates" not in self.payload:
            self.payload["bookingdates"] = {}
        self.payload["bookingdates"]["checkout"] = checkout_date
        return self

    def set_additional_needs(self, needs):
        self.payload["additionalneeds"] = needs
        return self

    def build(self):
        return self.payload