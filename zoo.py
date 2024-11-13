class Zoo:
    def get_ticket_price(self, age):
        # fix condition add 0
        if 0 <= age <= 12:
            return 50
        # fix condition add 20 
        elif 13 <= age <= 20:
            return 100
        # fix condition add 21
        elif 21 <= age <= 60:
            return 150
        # fix condition remove 60
        elif age > 60:
            return 100
        # in case that it is not in condition
        return 0