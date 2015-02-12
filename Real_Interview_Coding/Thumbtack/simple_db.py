__author__ = 'daming'

import fileinput

class TransactionBlock:
    def __init__(self):
        self.my_map= {}
        self.my_reverse_map = {}

    def set_key(self, key, val):
        prev_val = None
        if key in self.my_map:
            prev_val = self.my_map[key]
        self.my_map[key] = val

        if val in self.my_reverse_map:
            self.my_reverse_map[val] += 1
        else:
            self.my_reverse_map[val] = 1

        if prev_val!=None:
            self.my_reverse_map[prev_val] -= 1

    def get_key(self, key):
        if key in self.my_map:
            return self.my_map[key]
        return "NULL"

    def unset_key(self, key):
        if key in self.my_map:
            its_val = self.my_map[key]
            del self.my_map[key]
            self.my_reverse_map[its_val] -= 1

    def num_equal_to(self,num):
        if num in self.my_reverse_map:
            return self.my_reverse_map[num]
        return 0

class SimpleDataBase:
    def __init__(self):
        self.transactions = []

    def deepCopyTransBlock(self, newone, oldone):
        for key in oldone.my_map:
            newone.my_map[key] = oldone.my_map[key]

        for key in oldone.my_reverse_map:
            newone.my_reverse_map[key] = oldone.my_reverse_map[key]

    def process(self):
        basic_trans_block = TransactionBlock()
        self.transactions.append(basic_trans_block)

        for line in fileinput.input():
            pieces = line.split()
            # SET a 10
            if len(pieces)==3 and pieces[0]=='SET':
                self.transactions[-1].set_key(pieces[1], pieces[2])
            # GET a
            elif pieces[0] == 'GET':
                print self.transactions[-1].get_key(pieces[1])
            # UNSET a
            elif pieces[0] == 'UNSET':
                self.transactions[-1].unset_key(pieces[1])
            # NUMEQUALTO 10
            elif pieces[0] == 'NUMEQUALTO':
                print self.transactions[-1].num_equal_to(pieces[1])
            # BEGIN
            elif pieces[0] == 'BEGIN':
                newone = TransactionBlock()
                self.deepCopyTransBlock(newone, self.transactions[-1])
                self.transactions.append(newone)
            # ROLLBACK
            elif pieces[0] == 'ROLLBACK':
                if len(self.transactions)==1:
                    print 'NO TRANSACTION'
                else:
                    self.transactions.pop()
            # COMMIT
            elif pieces[0] == 'COMMIT':
                if len(self.transactions)==1:
                    print 'NO TRANSACTION'
                else:
                    self.deepCopyTransBlock(self.transactions[0], self.transactions[-1])
                    self.transactions = self.transactions[0:1]
            # END
            elif pieces[0] == 'END':
                return

obj = SimpleDataBase()
obj.process()