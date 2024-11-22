
import sys
import person

def main():
    c = person.Person("A", 50)
    u = person.Person("B", 60)
    c.inage(20)
    u.inage(20)

    print(f" Info of a - {c.name} {c.age} ")
    print(f" Info of b - {u.name} {u.age}")
    # Override add
    print(f" A + B age is {c.age + u.age}")

    # set value using option 1 getter and setter
    c.setage(100)
    print(f" A get age c.getage() - {c.getage()}")

    c.personage = 100
    print(f" A get age c.personage - {c.personage}")

    # set value using option 2 getter and setter
    c.personname = "C"
    print(f" A get age c.personname - {c.personname}")

    print(f" B Info - {u}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)