from Strategy import *
import itertools

def generate_all_strategies(n:int, l:int, k:int, winning_for_Questioner:bool = False):
    """
    This function acts as a generator for all possible strategies given certain n, l, and k.
    
    Parameters
    ----------
    n : int
        The size of the total guessing space {1, 2, ..., n}.
    l : int
        The length of each question in the strategy.
    k : int
        The number of questions in each strategy.
    winning_for_Questioner : bool, optional
        If True, then the generator will only return strategies that are winning for the Questioner.
        If False, then the generator will return all strategies, regardless of who wins.
    """
    
    # Generator for all questions
    def question_generator():
        for question in itertools.combinations(range(1, n + 1), l):
            yield Question(question)

    # Generator for all strategies
    def strategy_generator():
        for questions in itertools.combinations(question_generator(), k):
            yield Strategy(questions, n)
    
    # Yield strategies based on the condition in winning_for_Questioner
    for strategy in strategy_generator():
        if not winning_for_Questioner or strategy.is_winning_for_Questioner():
            yield strategy

def generate_circulant_strategies(n:int, l:int, k:int, winning_for_Questioner:bool = False):
    """
    This function generates all circulant strategies, where a strategy is built 
    by cyclically shifting the components of the first question. 

    Parameters
    ----------
    n : int
        The size of the total guessing space {1, 2, ..., n}.
    l : int
        The length of each question in the strategy.
    k : int
        The number of questions in each strategy.
    winning_for_Questioner : bool, optional
        If True, only returns strategies that are winning for the Questioner.
        If False, returns all circulant strategies regardless of the outcome.
    """
    
    # Generator for all questions
    def question_generator():
        for question in itertools.combinations(range(1, n + 1), l):
            yield Question(question)

    # Generator for all strategies created by circulating the first row
    def circulant_strategy_generator():
        for initial_question in question_generator():
            questions = [initial_question]
            for _ in range(l - 1):
                previous_question_components = questions[-1].components
                next_question = [(i + 1) if i != n else 1 for i in previous_question_components]
                questions.append(Question(next_question))
            yield Strategy(questions, n)
            
    # Yield strategies based on the condition in winning_for_Questioner
    for strategy in circulant_strategy_generator():
        if not winning_for_Questioner or strategy.is_winning_for_Questioner():
            yield strategy