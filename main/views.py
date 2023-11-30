from dj_rest_auth.views import LoginView


class CustomLogin(LoginView):
    def get_response(self):
        response = super().get_response()
        print("test")
        return response
