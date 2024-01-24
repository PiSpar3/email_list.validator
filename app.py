import re

#email="james@email.com"

# create your pattern
#pattern = re.compile(r"\w{2,}@\w{4,}\.com")

#pattern = re.compile(r"\w+@\w+\.\w+")

email = "james@.com"

pattern = re.compile(r"\w+@[.&]com")

result = pattern.search(email)

print(result)