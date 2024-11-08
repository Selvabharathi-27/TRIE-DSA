class node():
    def __init__(self):
        self.children={}
        self.isend=False
class trie():
    def __init__(self):
        self.root=node()
    def insert(self,word):
        current=self.root
        for i in word:
            if i not in current.children:
                current.children[i]=node()
            current=current.children[i]
        current.isend=True
    def search(self,word):
        current=self.root
        for i in word:
            if i not in current.children:
                print("False no word is there")    
                return 
            current=current.children[i]
        if current.isend==True:
            print("True")
        else:
            print("False")
    def display(self):
        def show(current,word):
            if current.isend:
                print(word)
            for i,j in current.children.items():
                show(j,word+i)
                
        show(self.root,"")
    def remove(self,word):
        if not  self.search(word):
            return
        stack=[]
        current=self.root
        for i in word:
            stack.append(current)
            current=current.children[i]
        current.isend=False
        while len(stack)>0:
            prev=stack.pop()
            last=word[len(stack)]
            if not prev.children[last].isend and not prev.children[last].children:
                del prev.children[last]
            else: break
      
trienode=trie()
trienode.insert("Apple")
trienode.insert("Application")
trienode.insert("App")
trienode.search("Apple")
trienode.remove("Appi")
trienode.display()  
