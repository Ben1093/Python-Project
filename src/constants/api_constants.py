class API_Constants():

    def get_booking(id):
        return "https://gorest.co.in/public/v2/users/" + str(id)

    def create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def update_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking" + "/" + str(booking_id)

