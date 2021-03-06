from enum import Enum

class InstrumentType(Enum):
    '''
    Defines three types for musical instruments.
    '''
    PERCUSSION = 'p'
    STRINGS = 's'
    WIND = 'w'    

class Instrument:
    '''
    This defines a musical instrument with the name of
    the instrument and its classification.
    '''
    def __init__(self, name, classification):
        '''
        Creates a new instrument. The name and
        classification of the instrument are required
        parameters.
        '''
        self.name = name
        if isinstance(classification, InstrumentType):
            self.classification = classification
        else:
            raise ValueError("Invalid value for instrument type: {}".format(classification))

    def getClassification(self):
        '''
        Returns the classification of the musical instrument.
        '''
        return self.classification

    def getName(self):
        '''
        Returns the name of the musical instrument.
        '''
        return self.name

    def setClassification(self, classification):
        '''
        Sets the classification of the musical instrument.
        '''
        if isinstance(classification, InstrumentType):
            self.classification = classification
        else:
            raise ValueError("Invalid value for instrument type: {}".format(classification))

    def setName(self, name):
        '''
        Sets the name of the musical instrument.
        '''
        self.name = name

    def __gt__(self, other):
        '''
        Convenience function for comparison between
        instruments.
        '''
        return self.name > other.getName()

    def __lt__(self, other):
        '''
        Convenience function for comparison between
        instruments.
        '''
        return self.name < other.getName()

class SLLNode:
    '''
    This defines a node in a singly-linked list. The node
    contains a data component and a nextnode reference. By
    default, data and nextnode are None.
    '''
    def __init__(self, data=None, nextnode=None):
        '''
        Creates a new node in the singly-linked list. If
        there is no data or nextnode passed, the values
        default to None.
        '''
        self.data = data
        self.nextnode = nextnode

    def getData(self):
        '''
        Returns the object the node contains.
        '''
        return self.data

    def getNext(self):
        '''
        Returns the reference to the next node.
        '''
        return self.nextnode

    def setData(self, data):
        '''
        Sets the object the node contains.
        '''
        self.data = data

    def setNext(self, nextnode):
        '''
        Sets the reference to the next node.
        '''
        self.nextnode = nextnode

class SLList:
    '''
    INSTRUCTIONS: As a class, write the methods and the
    documentation for these for a fully-working
    singly-linked list.
    '''
    def __init__(self, head = None):
        '''
        Create an empty list if there is no node passed to
        the constructor. Otherwise, create a list with the
        node passed.
        '''
        self.head = head

    def countInstances(self, data):
        # Count the number of times 
        pass

    def delete(self, data):
        '''
        Deletes the node and returns True if the node is
        found. If the node is not found in the list, the
        function returns False.
        '''
        # Hint: you can use search.
        pass

    def deleteAtHead(self):
        pass

    def deleteAtTail(self):
        pass

    def insert(self, data):
        '''
        Inserts a node at the end of the list.
        '''
        if isinstance(data, SLLNode):
            # insert more code here
            pass
        else:
            newNode = SLLNode(data)
        # insert more code here

    def insertAfter(self, data, newdata):
        # Look for the instance of data and add a new node
        # after it with newdata.
        pass

    def insertBefore(self, data, newdata):
        # Look for the instance of data and add a new node
        # before it with newdata.
        pass

    def insertAtHead(self, data):
        '''
        Inserts a node at the start of the list.
        '''
        # insert more code here
        pass

    def insertAtTail(self, data):
        '''
        Inserts a node at the tail of the list.
        '''
        # insert more code here
		currNode = self.head
		while currNode.getNext() == not None:
			currNode = currNode.getNext()
		
		currNode.setNext(data)
        pass

    def insertInOrder(self, data):
        # Insert a new node assuming that the list is in
        # ascending order and the order is preserved.
		currNode = self.head
		while currNode.getNext() == not None:
			if (currNode.getNext().getData() > data) and (currNode.getData() <= data):
				nextNode = currNode.getNext()
				dataNode = data
				currNode.setNext(dataNode)
				dataNode.setNext(nextNode)
				break
			else:
				currNode = currNode.getNext()
        pass

    def getSize(self):
		currNode = self.head
		count = 0
		while currNode.getNext() == not None:
			count += 1
			currNode = currNode.getNext()
		
		return count
        pass

    def search(self, data):
        # ValueError("Item {} not found".format(str(data)))
        # should be raised if the data is not found. If it
        # is found, the reference to the node is returned.
		currNode = self.head
		while currNode.getNext() == not None:
			if currNode.getData() == data:
				return currNode
			
			currNode = currNode.getNext()
		
		raise ValueError("Item {} not found".format(str(data)))
        pass

one = Instrument("Guitar", InstrumentType.STRINGS)
two = Instrument("Oboe", InstrumentType.WIND)
print(one < two)
