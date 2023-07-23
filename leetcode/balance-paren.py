def checkparen(str):
    parens={
            "(": ")",
            "{": "}",
            "[": "]"
    }
    closedParen=parens.values()

    myStack=[]
    for c in str:
        if c in parens:
            expectChar=parens[c]
            myStack.append(expectChar)
        elif c in closedParen:
            if myStack == [] or c != myStack.pop():
                return False
    
    return myStack == []


print ( checkparen("{}"))
print ( checkparen("{[]}"))
print ( checkparen("{[]}}"))
print ( checkparen("{{[]}}"))
print ( checkparen("{}[]()]][["))


print ( checkparen("{133}"))
print ( checkparen("{"))
print ( checkparen("{]"))
print ( checkparen("{()()[}"))

