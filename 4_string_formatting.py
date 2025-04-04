name = 'Juan'
age = 25

# % operator, similar to C
print("Hi %s, you are %s years old" % (name, age))

# Python 3 format method
greeting_str = "Hi {name}, you are {age} years old".format(name=name, age=age)
print(greeting_str)

# f strings (Python 3.6+)
greeting_str = f"Hi {name}, you are {age} years old"
print(greeting_str)

# join
age_str = str(age)
words = [name, age_str]
two_words_joined = " ".join(words)
print(two_words_joined)

# Concatenation
greeting_str = "Hi " + name + ", you are " + str(age) + " years old"
print(greeting_str)