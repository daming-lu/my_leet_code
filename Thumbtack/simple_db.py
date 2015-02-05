__author__ = 'daming'

import fileinput
import copy
class TransactionBlock:
    def __init__(self):
        self.my_map= {'t1':1, 't2':1}
        self.my_reverse_map = {1:2}

    def  __str__(self):
        result = ""
        # print 'my_map: '
        result += '\nmy_map: \n'
        for key in self.my_map:
            # print '\t', key, ' => ', self.my_map[key]
            result += ('\n'+key+ ' => '+ str(self.my_map[key])+'\n')
        # print '\nmy_reverse_map: \n'
        result += '\nmy_reverse_map: \n'
        for key in self.my_reverse_map:
            # print '\t', key, ' => ', self.my_reverse_map[key]
            result += ('\n'+str(key)+ ' => '+ str(self.my_reverse_map[key])+'\n')
        return result

    def __deepcopy__(self, memo):
        newone = TransactionBlock()
        newone.__dict__.update(self.__dict__)
        for key in self.my_map:
            newone.my_map[key] = self.my_map[key]

        for key in self.my_reverse_map:
            newone.my_reverse_map[key] = self.my_reverse_map[key]
        return newone

class SimpleDataBase:
    def __init__(self):
        self.transactions = []

    def process(self):
        basic_trans_block = TransactionBlock()
        clone1 = copy.deepcopy(basic_trans_block)
        print '\nbasic_trans_block ',basic_trans_block
        print '\nclone1 ',clone1

        self.transactions.append(basic_trans_block)
        print '\nOver here:\n'
        for line in fileinput.input():
            print line, ' * '
            
        print '\n\n'



obj = SimpleDataBase()
obj.process()