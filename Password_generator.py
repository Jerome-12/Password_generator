import random
import string

lenght=12
password=''.join(random.choices(string.ascii_letters + string.digits, k=lenght))
print("password : ", password)
