#!/user/bin/ev python3
""" Jerad Alexander | This this is my Character/parent Class"""

#standard libraries

#3rd party libraries
from Character_file import Character

##if __name__ == '__main__':

class Monster(Character):
    """This is the adventurer class"""
    def __init__(self,name,HP,weakness):
       super().__init__(name,HP)
       self.weakness = weakness
    
    
        
            
    
        

    