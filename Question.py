
class Question:
    '''
    A class to represent a question in some strategy.
    These questions are subsets of the total guessing space {1, 2, ..., n}.
    
    Attributes
    ----------
    components : set
        the set of numbers included in the question.
        
    Methods
    ----------
    answer_question(R):
        Given the responders choices R = (a,b), answers the question with either 0, 1, or 2.
    complement():
        Returns the complementary question, being the question with all of the numbers not included.
    add_number():
        Returns a new Question with the given number inserted into it.
    '''
    def __init__(self, components:set[int]) -> None:
        self.components = set(components)
    
    # Methods
    def answer_question(self, R:tuple[int,int]) -> int:
        '''
        Given a pair of numbers (a,b), returns how many times the pair occurs n the question set.
        That is, answers the question "How many of your numbers appear in the question set?"
        
        Parameters
        ----------
        R : tuple[int,int]
            A pair of numbers, say (a,b) where a,b are integers in the guessing space. These are the numbers that the Responder would have chosen when answering the questions. 
        '''
        
        # R = (a,b)
        a, b = R
        
        # Sum the appearances of a and b in the components
        count = 0
        if a in self.components:
            count += 1
        if b in self.components:
            count += 1
            
        return count
    
    def complement(self, n:int) -> 'Question':
        '''
        Returns the complement question. That is, returns a Question object that includes all of the components in the guessing space not found in the "parent" question.
        
        Parameters
        ----------
        n : int
            the maximum number in the total guessing space
        '''
        
        # Define the guessing space S = {1, 2, ..., n}
        S = set([i for i in range(1, n+1)])
        
        # Remove all of the numbers in the original question, which gives us the numbers in the complement question
        complement_components = S - self.components
        
        return Question(complement_components, n)
    
    def add_number(self, i:int) -> 'Question':
        '''
        This function returns a new Question object with the given number added to it.
        
        Parameters
        ----------
        i : int
            The integer that you want to add to the Question.
        '''
        components = list(self.components)
        components.append(i)
        return Question(components)
    
    # Magic Methods
    def __str__(self):
        return str(self.components)
    
    def __len__(self):
        return len(self.components)
    
    def __contains__(self, item):
        # If the item is an integer, return True if the question contains that integer
        if type(item) == int:
            return item in self.components
        
        # If the item is a Question, return True if all of the components in item are components in this Question
        elif type(item) == Question:
            return all([i in self.components for i in item.components])
        
        else:
            raise TypeError()
