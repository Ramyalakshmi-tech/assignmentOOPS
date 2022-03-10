class Registration():
    def Password(self):
        print("Your Password is saved")

class ForgotPassword(Registration):
    def Password(self):
        super().Password()
        print("This is your newPassword")

obj=ForgotPassword()
obj.Password()