def hello(to):
    print("hello",to)

name = input("what's your name? " )

# Remove Whitespace and capitalize each word
name = name.strip().title()
hello(name)
