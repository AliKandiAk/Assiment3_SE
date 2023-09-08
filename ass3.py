class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop()

    def palindrome(self):
        b = []
        for a in self.elements:
            b.append(a)
        self.elements.reverse()  # Reverse the original list in-place
        if b == self.elements:
            return True
        else:
            return False

    def is_empty(self):  # check if stack empty 
        return len(self.elements) == 0

    def is_balanced(self, expression):
        open_brac = "([{"
        close_brac = ")]"
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for char in expression: # check every charecter in expression 
            if char in open_brac:# check char in open brac
                self.push(char)
            elif char in close_brac: # check if char in closed brac
                if self.is_empty() or bracket_pairs[char] != self.pop():
                    return False

        return self.is_empty()

s = Stack()
#1
s.push(1)
s.push(2)
s.push(1)

print(s.palindrome())
#2
print(s.is_balanced("(1+2)-3*[41+6]"))  # True
print(s.is_balanced("(1+2)-3*[41+6}"))  # False
print(s.is_balanced("(1+2)-3*[41+6"))   # False
print(s.is_balanced("(1+[2-3]*4{41+6})"))  # True
print(s.is_balanced("(1+2)-3*]41+6["))  # False

#STACK
#STACK
def decode_message(message):
    stack = Stack()
    decod_msg = ""

    for char in message:
        if char.isalpha() or char.isspace(): # check for apphabetical order and spaces
            stack.push(char) 
        elif char == "*":
            popped_char = stack.pop()
            if popped_char:
                decod_msg += popped_char

  
    while not stack.is_empty():# pop the remaining charecters
        popped_char = stack.pop()
        if popped_char:
            decod_msg += popped_char

    return decod_msg


message = "SIVLE ****** DAED TNSI ***"
decoded_message = decode_message(message)
print(decoded_message)

####################
#QUEUES
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addToTail(self, info):
        n = Node(info)
        if self.size == 0:
            self.head = n
            self.tail = n
            self.size += 1
        else:
            self.tail.next = n
            self.tail = n
            self.size += 1

    def deleteHead(self):
        if self.size == 0:
            return None
        if self.size == 1:
            temp = self.head.info
            self.head = None
            self.tail = None
            self.size = 0
            return temp
        temp = self.head.info
        self.head = self.head.next
        self.size -= 1
        return temp

    def deleteCar(self, plate_number):
        if self.size == 0: # check if empty 
            return None
        if self.size == 1 and self.head.info.plate_number == plate_number:# check if plate number found 
            temp = self.head.info  
            self.head = None
            self.tail = None
            self.size = 0
            return temp
        prev = None
        current = self.head
        while current is not None:
            if current.info.plate_number == plate_number:
                if current == self.head:
                    self.head = current.next
                elif current == self.tail:
                    self.tail = prev
                    prev.next = None
                else:
                    prev.next = current.next
                self.size -= 1
                return current.info
            prev = current
            current = current.next
        return None


class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class Car:
    def __init__(self, make, color, plate_number):
        self.make = make
        self.color = color
        self.plate_number = plate_number

    def __str__(self):
        return f"Make: {self.make}, Color: {self.color}, Plate Number: {self.plate_number}"


class Queue:
    def __init__(self):
        self.elements = LinkedList()

    def enqueue(self, car):
        self.elements.addToTail(car)

    def dequeue(self):
        return self.elements.deleteHead()

    def size(self):
        return self.elements.size

    def isEmpty(self):
        return self.elements.size == 0

    def front(self):
        if self.elements.head is not None:
            return self.elements.head.info
        else:
            return None


queue = Queue()

while True:
    print("\nMenu:")
    print("1. Insert a car: ")
    print("2. Remove a car: ")
    print("3. Quit: ")

    choice = input("Enter your choice: ")

    if choice == '1':
        make = input("Enter the make of the car: ")
        color = input("Enter the color of the car: ")
        plate_number = int(input("Enter the plate number of the car: "))
        car = Car(make, color, plate_number)
        queue.enqueue(car)
        print(f"{car} has been added to the queue.")

    elif choice == '2':
        plate_number = int(input("Enter the plate number of the car to remove: "))
        removed_car = queue.elements.deleteCar(plate_number)
        if removed_car is not None:
            print(f"The following car has been removed from the queue:")
            print(removed_car)
        else:
            print("No car found with that plate number.")

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please try again.")



