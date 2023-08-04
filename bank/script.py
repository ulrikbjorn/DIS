
print(2)


from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
a = bcrypt.generate_password_hash("memestock")

print(a)