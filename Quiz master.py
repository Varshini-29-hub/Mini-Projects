import time

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")
    
# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What does the acronym JVM stand for ?",
        "options": ["A. Java Virtual Machine", "B. Java Visual Machine", "C.JRE Virtual Machine", "D. JRE Visual Machine"],
        "answer": "A"
    },
    {
        "prompt": "what do we call locating or indentifying the bugs in softwae testing ?",
        "options": ["A. Design", "B. Debugging", "C. Testing", "D. Coding"],
        "answer": "C"
    },
    {
        "prompt": "The Sum Of The First Prime Numbers are?",
        "options": ["A. 11", "B. 18", "C. 26", "D. 28"],
        "answer": "D"
    },
    {
        "prompt": "What does the term API stand for in the context of programming?",
        "options": ["A. Advanced Program Integration", "B. Application Programming Interface", "C. Automated Program Interaction", "D. Advanced Programming Interface"],
        "answer": "B"
    },
    {
        "prompt": "which command is used to create a new table in SQL?",
        "options": ["A. Build Table", "B. Create Table", "C. General Table", "D. None Of The Above"],
        "answer": "B"
    },
    {
        "prompt": "why were cookies designed?",
        "options": ["A. For server-side programming", "B. For Client-side programming", "C.Both a and b", "D. None"],
        "answer": "A"
    },
    {
        "prompt": "What does the acronym URL stand for in the context of web development?",
        "options": ["A. Universal Resource Locator", "B. Unified Resource Locator", "C. Uniform Resource Locator", "D. Unique Resource Locator"],
        "answer": "C"
    },
    {
        "prompt": "Which of the following is not a valid loop statement in Java?",
        "options": ["A. for", "B. while", "C. loop", "D. do-while"],
        "answer": "C"
    },
    {
        "prompt": "What is Git?",
        "options": ["A. Text Editor", "B. Compiler", "C. Version Control system", "D. Operating System"],
        "answer": "C"
    },
    {
        "prompt": "Which of the following data structures follows the First-In-First-Out (FIFO) principle?",
        "options": ["A. Queue", "B. Stack", "C. Linked List", "D. Array"],
        "answer": "A"
    },
]

# Run the quiz
run_quiz(questions)
