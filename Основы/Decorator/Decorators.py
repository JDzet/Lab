def  hader(func):

    def inner(*args, **kwargs):
        print("<hader>")
        func(*args, **kwargs)
        print("</hader>")
    return inner

def table(func):
    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    return inner

@hader
@table # say = header(table(say))
def say(name,surname, age):
    print("Hello ", name, surname, age)



say('Vasya','Ivanov', 23) # вызов