class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}]"

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node
        print("Its a push method"f'{self.begin},{self.end}')
        self.print()

    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            # assert self.end != node
            self.end = node
            value = node.next.value
            node.next = None
            return value

    def shift(self, obj):
        """Another name for push."""
        node = SingleLinkedListNode(obj,None)
        if self.end == None:
            self.end = node
            self.begin = self.end
        else:
            node.next = self.begin
            self.begin = node
        print("Its a Shift" f'{self.begin},{self.end}')
        self.print()

    def print(self):
        output = []
        curr = self.begin
        while curr:
            output.append(curr.value)
            curr = curr.next
        print("The list is: ",output)


    def unshift(self):
        """Removes the first item and returns it."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""

colors = SingleLinkedList()
colors.push('Blue')
colors.push('Green')
colors.push('Violet')
colors.push('Purple')
print("pop here: ",colors.pop())
colors.print()
colors.push('Orange')
print(colors.count())
print("the first element:",colors.first())
print("the last element:",colors.last())
colors.shift('Orange')
colors.shift('Green')
