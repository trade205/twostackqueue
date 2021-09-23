stackData = [1,2,3,4,5]
stackMin = []
class GetMin(object):

    def push_item(newNum):
        if len(stackMin) == 0:
            stackMin.append(newNum)
        elif newNum <= getmin():
            stackMin.append(newNum)
        stackData.append(newNum)

    def pop_item(self):
        if len(stackData) == 0 :
            print("stack is empty")
        value = stackData.pop()
        if value == getmin():
            stackMin.pop()
        return value

    def getmin():
        if len(stackMin) == 0:
            print("stack is empty")
        return stackMin.pop()

if __name__ == '__main__':
    text = GetMin()
    text.pop_item()
    text.getmin()


