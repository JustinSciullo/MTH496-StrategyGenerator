from Question import *
from sympy import Matrix

class Strategy:
    '''
    A class to represent an offline guessing game strategy. In essence, it represents a set of Question objects along with several methods.
    
    Attributes
    ----------
    questions : set
        An iterable of iterables, which is turned into a set of Question objects.
    n : int
        The maximum number in our guessing space S = {1, 2, ..., n}
        
    Methods
    ----------
    answer_questions(R):
        Given the responders choice R = (a,b), returns the answer vector for each question.
    is_winning_for_Questioner(print_information=False):
        Returns True if the strategy is winning for the Questioner, and False otherwise.
    complement():
        Returns the complementary strategy. That is, returns a strategy with the complimentary questions.
    strategy_matrix()
        Returns the strategy matrix as a sympy.Matrix object.
    '''
    def __init__(self, questions, n:int) -> None:
        
        self.n = n
        
        # Find the first question in our set
        first_question = list(questions)[0]
        
        # Case 1: Question object
        if type(first_question) == Question:
            self.questions = list(questions)
        
        # Case 2: List/Tuple/Set object
        elif type(first_question) in (set, list, tuple):
            
            # Turn each question iterable into a Question
            if type(first_question) in (list, tuple):
                questions = [Question(set(q)) for q in questions]
                self.questions = questions
        
        # Case 3: Invalid type for questions
        else:
            raise TypeError("Invalid type for questions, please input an iterable of iterables (list of lists)!")


    def answer_questions(self, R:tuple[int,int]) -> tuple:
        answer_vector = [q.answer_question(R) for q in self.questions]
        return tuple(answer_vector)

    def is_winning_for_Questioner(self, print_information=False) -> bool:
        
        # Create a generator of every possible pair of numbers the Responder can choose
        def all_responder_pairs():
            for a in range(1, self.n + 1):
                for b in range(a + 1, self.n + 1):
                    yield (a,b)
        
        # Create a list to keep track of every answer vector per possible R
        answer_vectors = []
        
        # Create an initially True boolean to return at the end of our loop
        winning_for_Questioner = True
        
        # Loop over every possible choice the Responder can make
        for R in all_responder_pairs():
            
            # Answer every question
            answer_vector = self.answer_questions(R)

            # Check if we have duplicate answer vectors
            if answer_vector in answer_vectors:
                
                # We have a duplicate, so the Responder wins :(
                winning_for_Questioner = False
                
            # Add the new answer vector and continue checking
            answer_vectors.append(answer_vector)
        
        # If we want to print the information, then we do it here
        if print_information:
            
            # If the Questioner is winning
            if winning_for_Questioner:
                print("This is a winning strategy for the Questioner!")
            
            # If the Questioner is losing
            else:
                print("This is NOT a winning strategy for the Questioner")
                
                # Turn our generator into a list
                list_of_responder_pairs = [i for i in all_responder_pairs()]
                
                # Keep track of what R values not to print twice
                dont_use_these_R_values_again = []
                
                # Loop over every R value
                for i, R in enumerate(list_of_responder_pairs):
                    
                    # Find the R values answer vector
                    R_answer_vector = answer_vectors[i]
                    
                    # Loop over every R value again
                    for j, answer_vector in enumerate(answer_vectors):
                        R2 = list_of_responder_pairs[j]
                        
                        # Skip this R value if R2 = R or we have already printed R
                        if i == j or R2 in dont_use_these_R_values_again:
                            continue
                        
                        # Print information if there is a duplicate answer vector
                        elif R_answer_vector == answer_vector:
                            print(f"{R} and {R2} both have the answer vector {answer_vector}.")
                            dont_use_these_R_values_again.append(R)
        
        # If we never found a duplicate, then the Questioner wins :)
        return winning_for_Questioner
        
    def complement(self) -> 'Strategy':
        '''
        Returns the complementary strategy. That is, it returns a new strategy where each question is the complementary question.
        '''
        compliment_questions = [q.complement() for q in self.questions]
        return Strategy(compliment_questions, self.n)
    
    def strategy_matrix(self) -> Matrix:
        '''
        Returns the "strategy matrix" of our strategy using sympy.Matrix.
        
        The matrix has the columns corresponding to each question, and the rows corresponding to each possibke number the Responder can pick from {1,2,...,n}. So for the strategy matrix S, we define S[i,j] to be 1 if question i contains the number j, and 0 otherwise.
        '''
        
        # Define a list for our matrix
        strategy_matrix = []
        
        # Loop over each question
        for q in self.questions:
            question_row = []
            
            # Loop over each value from 1 to n
            for i in range(1, self.n+1):
                
                # If n is in the question, append 1
                if i in q:
                    question_row.append(1)
                else:
                    question_row.append(0)
                    
            # Add our row to our list of rows (matrix)
            strategy_matrix.append(question_row)
        return Matrix(strategy_matrix)
    
    def add_question(self, question:Question) -> 'Strategy': 
        current_questions = self.questions
        current_questions.append(question)
        return Strategy(current_questions, self.n)
    
    def copy(self) -> 'Strategy':
        return Strategy(self.questions, self.n)
  
    def __str__(self):
        string = ""
        for question in self.questions:
            string += question.__str__() + "\n"
        return string
    
    def __len__(self):
        return len(self.questions)