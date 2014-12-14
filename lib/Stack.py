class stack:
    def __init__(self):
        self.content=[]
        self.len=0

    def IsEmpty(self):
        if self.len==0:
            return True
        else:
            return False

    def Push(self,value):
        self.content.append(value)
        self.len=self.len+1

    def Pop(self):
        if self.IsEmpty():
            print "stack is empty"
        else:
            temp=self.content[self.len-1]
            del self.content[self.len-1]
            self.len=self.len-1
            return temp
