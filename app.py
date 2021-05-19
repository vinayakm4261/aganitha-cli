class Base:
    name = ""

    def __init__(self, name):
        self.name = name

    def execute(self, class_name, args):
        print("Execute from class: {} object: {} and arguments: {}".format(class_name, self.name, ",".join(args)))

    def shutdown(self, class_name):
        print("Shutdown from object: {} and class: {}".format(self.name, class_name))


class A(Base):
    class_name = "A"

    def __init__(self, name):
        super().__init__(name)
        print("Initialized object: {} of class: {}".format(name, self.class_name))

    def execute(self, args):
        super().execute(self.class_name, args)

    def shutdown(self):
        super().shutdown(self.class_name)


class B(Base):
    class_name = "B"

    def __init__(self, name):
        super().__init__(name)
        print("Initialized object: {} of class: {}".format(name, self.class_name))

    def execute(self, args):
        super().execute(self.class_name, args)

    def shutdown(self):
        super().shutdown(self.class_name)


class C(Base):
    class_name = "C"

    def __init__(self, name):
        super().__init__(name)
        print("Initialized object: {} of class: {}".format(name, self.class_name))

    def execute(self, args):
        super().execute(self.class_name, args)

    def shutdown(self):
        super().shutdown(self.class_name)


def print_menu():
    print("--------------------")
    print(
        "Actions:\n1.Create object\n2.Delete object\n3.Execute method\nEnter your choice:\nOR type 'quit' without quotes to exit"
    )
    print("--------------------")


def create_object(name, class_name):
    if class_name == "A":
        return A(name)
    elif class_name == "B":
        return B(name)
    else:
        return C(name)


print_menu()

choice = input()

objects = {}
obj_map = {}
class_count = {"A": 0, "B": 0, "C": 0}


def print_counts():
    print()
    print("{:<15} | {:>15}".format("Object name", "Invocations"))
    for obj in obj_map.keys():
        print("{:^15} | {:^15}".format(obj, obj_map[obj][1]))
    print()
    print("{:<15} | {:>15}".format("Class name", "Invocations"))
    for c_name in class_count.keys():
        print("{:^15} | {:^15}".format(c_name, class_count[c_name]))


while choice != "quit":
    if choice == "1":
        selected_class = input("Select class:\nA, B or C\nType the letter: ")

        if selected_class not in ["A", "B", "C"]:
            print("Invalid classname!")

        else:
            object_name = input("Enter name of the object to be created: ")
            print()

            objects[object_name] = create_object(object_name, selected_class)
            obj_map[object_name] = [selected_class, 0]
    elif choice == "2":
        object_name = input("Enter name of object to be deleted:")

        if object_name in objects.keys():
            del objects[object_name]
            del obj_map[object_name]
        else:
            print("Object does not exist!\n")
    elif choice == "3":
        object_name = input("Enter name of object: ")

        if object_name in objects.keys():
            args = input("Enter space separated arguments: ")
            print()

            objects[object_name].execute(args.split())

            obj_map[object_name][1] = obj_map[object_name][1] + 1

            object_class = obj_map[object_name][0]

            class_count[object_class] = class_count[object_class] + 1
        else:
            print("Object does not exist!")

    print_counts()
    print_menu()

    choice = input()
