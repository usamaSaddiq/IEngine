import Chaining,sys,KnowledgeBase
from TruthTable import handle

try:
    if len(sys.argv) != 3:
        raise Exception("Not enough arguments. Exiting with code 1")
    else:
        sentences = None
        query = None
        with open(sys.argv[2]) as f:
            next(f)
            for line in f:
                sentences = line.rstrip()
                sentences = sentences.split(";")
                sentences = [x for x in sentences if x]   
                next(f)
                query = f.readline()

        kb = KnowledgeBase.KnowledgeBase()
        for s in sentences:
            kb.feed_sentence(s)
        if sys.argv[1] == 'TT':
            handle(kb,query)
        if sys.argv[1] == 'FC':
            tool = Chaining.Chaining()
            result,trace = tool.get_fchain(kb, query)
            if result == True:
                print("Yes: ", end="")    
                for t in trace:
                    print(t.name + " ", end="")
            else:
                print("No")
        if sys.argv[1] == 'BC':
            tool = Chaining.Chaining()
            result,trace = tool.get_bchain(kb, query)
            if result == True:
                print("Yes: ", end="")    
                for t in trace:
                    print(t.name + " ", end="")
            else:
                print("No")

except Exception as e:
    print ("The following error occured. Exiting with code 1 \n {0}".format(e))
