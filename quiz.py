import time
python=["01.What is dictionary in python?",
         "02.Which keyword is used to handle exceptions?",
         "03.What keyword is used to exit a loop in python?",
         "04.Which of the following datatype is immutable?",
         "05.What does the range() function do?"]
options1=(("A.An ordered collection of items","B.An unordered collection of key value pairs","C.A collection of unique items","D.A sequence of characters"),
          ("A.Catch","B.Handle","C.Try","D.Except"),
          ("A.Stop","B.Exit","C.Break","D.end"),
          ("A.List","B.Dictionary","C.String","D.Set"),
          ("A.Creates a list of numbers","B.Generates a sequence of numbers","C.Returns the length of a list","D.Sorts a list"))
answers1=("B","C","C","C","B")
level2_python=["1.Which of the following will raise a TypeError?",
               "2.Which of the following correctly defines a decorator in python?",
               "3.Which of the following is NOT a valid way to import a module?",
               "4.Which of the following is true about the __init__ method?",
               "5.Which of the following methods can be used to sort a list?"]
options5=(("A.1+'1'","B.len(123)","C.int('abc')","D.none+1"),
          ("A.A function that adds functionality to another function","B.A special type of class","C.A method that modifies an object","D.A way to create variables"),
          ("A.import module","B.from module import * ","C.import module as alias","D.include module"),
          ("A.It i a destructor mothod","B.It initializes an object's attributes","C.It is called explicitly","D.It cannot take parameters"),
          ("A.list.sort()","B.sorted(list)","C.both a and b","D.none of the above"))
answers5=("A","A","D","B","C")
maths=["1.What is the next number in the sequence:2,6,12,20,30,....?",
       "2.Find the odd one out:6,11,17,23,29,34.",
       "3.If the day before yesterday was Thursday,what day will it be tomorrow?",
       "4.What is next number in the series:3,6,11,18,27,...?",
       "5.What comes next in the series:10,15,21,28,36,...?"]
options2=(("A.40","B.42","C.36","D.46"),
          ("A.6","B.17","C.29","D.34"),
          ("A.Saturday","B.Sunday","C.Monday","D.Tuesday"),
          ("A.36","B.38","C.40","D.46"),
          ("A.41","B.45","C.51","D.55"))
answers2=("B","D","A","A","B")
dsa=["1.Which data structure follows the LIFO principle?",
     "2.Which data structure is used to implement recursion?",
     "3.Which of the following is NOT a linear data structure?",
     "4.What is the maximum number of children a binary tree node can have?",
     "5.Which data structure is used to implement a priority queue?"]
options3=(("A.Queue","B.Stack","C.Array","D.Linked list"),
          ("A.Queue","B.Stack","C.Tree","D.Graph"),
          ("A.Stack","B.Queue","C.Linked list","D.Tree"),
          ("A.1","B.2","C.3","D.4"),
          ("A.Stack","B.Array","C.Heap","D.Linked list"))
answers3=("B","B","D","B","C")
level2_dsa=["1.What is the time complexity of inserting an element at the end of a singly linked list (assuming we have access to the tail)?",
            "2.Which of the following sorting algorithms has the best average-case time complexity?",
            "3.What data structure would you use for a Breadth-First Search (BFS) traversal of a graph?",
            "4.Which of the following operations is the most time-efficient for a Hash Map?",
            "5.Which of the following data structures does not allow duplicate elements?"]
options6=(("A.O(1)","B.O(n)","C.O(log n)","D.O(n log n)"),
          ("A.Quick Sort","B.Merge Sort","C.Bubble Sort","D.Selection Sort"),
          ("A.Stack","B.Queue","C.Hash Table","D.Binary Search Tree"),
          ("A.Searching","B.Insertion","C.Deletion","D.All of the above"),
          ("A.Array","B.Stack","C.Queue","D.Set"))
answers6=("A","B","B","D","D")
level2_maths=["1.Pointing to a photograph, Ravi said,'She is the daughter of my grandfather's only son.'How is the girl in the photograph related to Ravi?",
              "2.Four friends, P, Q, R, and S, are sitting in a row. P is sitting next to Q, and R is not sitting next to S. S is sitting to the left of Q. Who is sitting on the extreme left?",
              "3.Book is to Reading as Pen is to:",
              "4.If a clock shows 3:15, what time will it show in the mirror?",
              "5.In a class of 40 students, Ravi ranks 7th from the top. What is his rank from the bottom?",
              "6.Five friends are sitting in a row. Ramesh is sitting next to Suresh. Suresh is sitting next to John, but not next to Peter. Peter is sitting next to Michael. Who is sitting on the extreme left?",
              "7.If A says,B's mother is the only daughter of my mother,how is A related to B?",
              "8.If the word TIME is written on paper and placed in front of a mirror, how will it appear in the mirror?",
              "9.Pointing to a man, Ram says,'His mother is the only daughter of my mother.'How is Ram related to the man?",
              "10.A boy says,'I have as many brothers as sisters.'His sister says,'I have twice as many brothers as sisters.'How many brothers and sisters are there?",]
options4=(("A.Sister","B.Mother","C.Cousin","D.Aunt"),
          ("A.P","B.S","C.R","D.Q"),
          ("A.Writing","B.Drawing","C.Painting","D.Sketching"),
          ("A.8:45","B.9:45","C.8:15","D.9:15"),
          ("A.34","B.33","C.35","D.36"),
          ("A.Peter","B.Michael","C.John","D.Ramesh"),
          ("A.Father","B.Grandfather","C.Brother","D.Uncle"),
          ("A.EMIT","B.TMI","C.METI","D.IEMT"),
          ("A.Father","B.Brother","C.Grandfather","D.Uncle"),
          ("A.3 brothers, 4 sisters","B.4 brothers, 3 sisters","C.2 brothers, 4 sisters","D.4 brothers, 2 sisters"))
answers4=(("A.Sister\nExplanation:The grandfather's only son is Ravi's father,so the girl in the photograph is his sister."),
          ("B.S\nExplanation:S sits to the left of Q, and P is next to Q, leaving S on the extreme left."),
          ("A.Writing\nExplanation:A pen is used for writing, just as a book is used for reading."),
          ("A.8:45\nExplanation: The mirror image of 3:15 would be 8:45."),
          ("B.33\nExplanation: If Ravi ranks 7th from the top in a class of 40 students, his rank from the bottom is 40–7+1=34"),
          ("A.Peter\nExplanation: Peter sits on the extreme left, followed by Michael, John, Suresh, and Ramesh."),
          ("A.Father\nExplanation: B’s mother is the only daughter of my mother means A is B’s father."),
          ("A.EMIT"),
          ("A.Father\nExplanation: The man is Ram's son."),
          ("B.4 brothers, 3 sisters\nExplanation: If the sister has twice as many brothers, the number of brothers must be 4 and sisters must be 3."))
answer4=("A","B","A","A","B","A","A","A","A","B")
def quiz_game():
    print("WELCOME TO QUIZ GAME!!!.....")
    while True:
        print("Categories are:\n1.Python\n2.Maths\n3.DSA(Data Structure and Algorithm)")
        category=int(input("Enter your category(1 or 2 or 3):"))
        question_num=0
        score=10
        time_limit=10
        default_answer="z"
        if(category==1):
            print("--------------------------------------------------------")
            print("WELCOME TO PYTHON QUIZ!!!.....")
            for i in python:
                print("--------------------------------------------------------")
                print(i)
                for j in options1[question_num]:
                    print(j)
                start_time = time.time()
                guess = input("Enter your correct option (you have 10 seconds): ").upper()
                elapsed_time = time.time() - start_time
                if elapsed_time > time_limit:
                    guess=default_answer
                    print(f"Time's up! You took {elapsed_time:.2f} seconds. The correct answer is: {answers1[question_num]}")
                    score-=2
                else:
                    if guess == answers1[question_num]:
                        print("Your answer is correct!")
                    else:
                        print("Your answer is wrong")
                        print("Your score is reduced by 2")
                        print("And the correct answer is:", answers1[question_num])
                question_num+=1
            print("Your Score is:",score)
            if(score>=5):
                print("Your are selected for next level")
                level2=int(input("Do you want to go to next level?(Press 1 to next level or press 2 to go back):"))
                print("-----------------------------------------------------------------------------")
                questions_num=0
                score=10
                if(level2==1):
                    print("Welcome to next level")
                    for i in level2_python:
                        print("-----------------------------------------------------------------------------")
                        print(i)
                        for j in options5[questions_num]:
                            print(j)
                        start_time = time.time()
                        guess = input("Enter your correct option (you have 10 seconds): ").upper()
                        elapsed_time = time.time() - start_time
                        if elapsed_time > time_limit:
                            print(f"Time's up! You took {elapsed_time:.2f} seconds. The correct answer is: {answers5[questions_num]}")
                            score-=2
                        else:
                            if(guess==answers5[questions_num]):
                                print("You guessed!")
                            else:
                                print("Wrong answer")
                                print("Answers is",answers5[questions_num])
                                score-=2
                        questions_num+=1
                    print("Your score is:",score)
                    if(score>=8):
                        print("Amazing!!!")
                    elif(score<5):
                        print("Nice try!")
                    else:
                        print("well done!")
            else:
                print("Your score is less than 5 try again to go to next level")
        elif(category==2):
            print("-----------------------------------------------------")
            print("WELCOME TO MATHS QUIZ!!!.....")
            for i in maths:
                print("-----------------------------------------------------")
                print(i)
                for j in options2[question_num]:
                    print(j)
                start_time = time.time()
                guess = input("Enter your correct option (you have 10 seconds): ").upper()
                elapsed_time = time.time() - start_time
                if elapsed_time > time_limit:
                    guess=default_answer
                    print(f"Time's up! You took {elapsed_time:.2f} seconds. The correct answer is: {answers2[question_num]}")
                    score-=2
                else:
                    if(guess==answers2[question_num]):
                        print("Your answer is correct!")
                    else:
                        print("Your answer is wrong")
                        score-=2
                        print("Your score is reduced by 2")
                        print("And the correct answer is:",answers2[question_num])
                question_num+=1
            print("Your Score is:",score)
            if(score>=5):
                print("Your are selected for next level")
                level2=int(input("Do you want to go to next level?(Press 1 to next level or press 2 to go back):"))
                print("-----------------------------------------------------------------------------")
                questions_num=0
                score=20
                if(level2==1):
                    print("Welcome to next level")
                    for i in level2_maths:
                        print("-----------------------------------------------------------------------------")
                        print(i)
                        for j in options4[questions_num]:
                            print(j)
                        start_time = time.time()
                        guess = input("Enter your correct option (you have 10 seconds): ").upper()
                        elapsed_time = time.time() - start_time
                        if elapsed_time > time_limit:
                            guess=default_answer
                            print(f"Time's up! You took {elapsed_time:.2f} seconds. The correct answer is: {answers4[questions_num]}")
                            score-=2
                        else:
                            if(guess==answer4[questions_num]):
                                print("You guessed!")
                            else:
                                print("Wrong answer")
                                print("Answers is",answer4[questions_num])
                                score-=2
                        questions_num+=1
                    print("Your score is:",score)
                    if(score>=8):
                        print("Amazing!!!")
                    elif(score<5):
                        print("Nice try!")
                    else:
                        print("well done!")
                    
            else:
                print("Your score is less than 5 try again to go to next level")
        elif(category==3):
            print("-----------------------------------------------------")
            print("WELCOME TO DSA QUIZ!!!.....")
            for i in dsa:
                print("-----------------------------------------------------")
                print(i)
                for j in options3[question_num]:
                    print(j)
                start_time = time.time()
                guess = input("Enter your correct option (you have 10 seconds): ").upper()
                elapsed_time = time.time() - start_time
                if elapsed_time > time_limit:
                    guess=default_answer
                    print(f"Time's up! You took {elapsed_time:.2f} seconds. The correct answer is: {answers3[question_num]}")
                    score-=2
                else:
                    if(guess==answers3[question_num]):
                        print("Your answer is correct!")
                    else:
                        print("Your answer is wrong")
                        print("Your score is reduced by 2")
                        print("And the correct answer is:",answers3[question_num])
                        score-=2
                question_num+=1
            print("Your Score is:",score)
            if(score>=5):
                print("Your are selected for next level")
                level2=int(input("Do you want to go to next level?(Press 1 to next level or press 2 to go back):"))
                questions_num=0
                score=10
                if(level2==1):
                    print("-----------------------------------------------------------------------------")
                    print("Welcome to next level")
                    for i in level2_dsa:
                        print("-----------------------------------------------------------------------------")
                        print(i)
                        for j in options6[questions_num]:
                            print(j)
                        start_time = time.time()
                        guess = input("Enter your correct option (you have 10 seconds): ").upper()
                        elapsed_time = time.time() - start_time
                        if elapsed_time > time_limit:
                            guess=default_answer
                            print(f"Time's up! You took {elapsed_time:.2f} seconds. The correct answer is: {answers6[questions_num]}")
                            score-=2
                        else:
                            if(guess==answers6[questions_num]):
                                print("You guessed!")
                            else:
                                print("Wrong answer")
                                print("Answers is",answers6[questions_num])
                                score=score-2
                        questions_num+=1
                    print("Your score is:",score)
                    if(score>=8):
                        print("Amazing!!!")
                    elif(score<5):
                        print("Nice try!")
                    else:
                        print("well done!")
            else:
                print("Your score is less than 5 try again to go to next level")
        else:
            print("Invalid category. Please choose 1, 2, or 3.")
        exit_game = int(input("Do you want to exit (Press 1 to exit, any other key to continue): "))
        if exit_game == 1:
            print("Thanks for playing!......")
            break
quiz_game()
       
            
            
            
    



    

