class Queue:
    def __init__(self):
        self.my_queue = []

    # add to the end of the queue
	def offer(self, el):
            self.my_queue.append(el)

    # return and remove the element at the front of the queue
	def poll(self):
            if len(self.my_queue)<1:
                return None
            return self.my_queue.pop(0)

    # return the element at the front of the queue
	def peek(self):
            if len(self.my_queue)<1:
                return None
            return self.my_queue[0]

class Stack:
    def __init__(self):
        self.my_queues = []
        self.my_queues.append(Queue())
        self.my_queues.append(Queue())
        self.cur_queue = 0


    # return the element at the top
    def peek(self):
        last_elem = None
        while True:
            cur_elem = self.my_queues[self.cur_queue].poll()
            if cur_elem == None:
                self.cur_queue = 1-self.cur_queue
                return last_elem
            self.my_queues[1-self.cur_queue].offer(cur_elem)
            last_elem = cur_elem

        self.cur_queue = 1-self.cur_queue
        return last_elem


    # return and remove the element at the top
    def pop(self):
        while True:
            cur_elem = self.my_queues[self.cur_queue].poll()
            if self.my_queues[self.cur_queue].peek() == None:
                self.cur_queue = 1-self.cur_queue
                return cur_elem
            self.my_queues[1-self.cur_queue].offer(cur_elem)

    # add el to the top
    def push(self, el):
        self.my_queues[self.cur_queue].offer(el)