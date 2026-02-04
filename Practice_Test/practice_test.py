def square_number(number : int)->int:
    """
    Your program should take in an integer and return that number squared.

    Args:
        number (int) : the number which must be squared.

    Returns:
        int : the square of the number
    """
    pass

def even_or_odd(number : int)-> str:
    """
    Your program should take in an integer and check if it is an 
    even number or an odd number.

    Args:
        number (int) : the number to be checked

    Returns:
        str : either 'odd' or 'even' 
    """
    if number % 2 == 0:
        return "even"
    elif number % 3 == 0:
        return "odd"
    pass

def get_highest (list : list[int])-> int:
    """
    Your program should take in a list or integers and find the highest number.
    DO NOT USE 'max' TO FIND THE HIGHEST!!

    Args:
        list (list[int]) : the list that contains all the numbers.

    Returns:
        int : the highest number
    """

    pass

def sum_of_list (list : list[int])-> int:
    """
    Your program should take in a list or integers and get the total of 
    all the numbers.
    DO NOT USE 'sum' TO GET THE TOTAL!!

    Args:
        list (list[int]) : the list that contains all the integers.

    Returns:
        int : the total of the list
    """
    if len(list) == list[0]:
        return list[0]
    return list[0] + sum_of_list(list[1:])
    

def first_and_last_letter (word : str) -> str:
    """
    Your program should take in a string and extract the first and last
    letters and output them as a string.

    e.g. given 'hello' return 'ho'

    Args:
        word (str) : the word that you will get the letters from

    Returns:
        str : the last and first letter as one string
    """
    pass

def count_letter (word : str, letter : str) -> int:
    """
    Your program should should take in a word and the letter, you must count the 
    amount of times that letter appears in the word.
    e.g. 
        var: word='hello' letter='l'
        return: 2

    Args:
        word (str) : the word that will be counted from
        letter (str) : the letter to count the amount of

    Returns:
        int : number of times the letter apears in the word

    """
    pass

def every_other_letter (word : str) -> str:
    """
    Your program should take in a word and then extraxt every second letter from
    the word then return it as a string.
    e.g. word = 'runner' return 'unr'

    Args:
        word (str) : the string that will be used to extract the letters

    Returns:
        str : combined string of all the second letters
    """
    pass

def strict_string(word : str) -> bool:

    """
    Strict String Requirements Challenge

    Your program should check that the word meets ALL of the following conditions:

    1. The word is at least 6 characters long.
    2. The word contains no digits.
    3. The word contains no spaces.
    4. The word contains both an "a" and an "e".
    5. The word starts with a consonant.
    6. The word ends with a vowel (a, e, i, o, u).
    7. The word contains at least one repeated letter (e.g., "tt" or "oo").

    If every condition is true, return true else return false.

    Args:
        word (str) : the word that will be checked.

    Returns:
        bool : true or false
    """
    pass