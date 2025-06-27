import secrets

import string as s 
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))

random = secrets.SystemRandom()
print(secrets.randbelow(100))
print(secrets.choice([10, 11, 12]))

random.seed(10)
