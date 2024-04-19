questions = [
    ["Which is the capital of India", "Delhi", "Punjab", "MH", "Kerala", 1],
    ["What is the national animal of India", "Lion", "Tiger", "Rabbit", "Fox", 2],
    ["What is the national bird of India", "Peacock", "Parrot", "Crow", "Sparrow", 1],
    ["What is the national currency of India", "USD", "DINAR", "DOLLAR", "INR", 4],
    ["Which team won the Cricket World Cup in 2023", "India", "SA", "AUS", "PAK", 3]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question {i+1}. {question[0]} ?")
    print(f"Above question for money is Rs. {levels[i]}")
    print(f"1. {question[1]}           2. {question[2]}")
    print(f"3. {question[3]}           4. {question[4]}")

    reply = input("Enter your answer between (1-4) or type 'quit' to end the quiz: ")

    if reply.lower() == 'quit':
        break

    reply = int(reply)

    if reply == question[-1]:
        print(f"Correct answer! You won Rs. {levels[i]}\n")
        money = levels[i]  # Update the money won
        
        # Check if it's the last question (index 4) to set the final money amount
        if i == 4:
            money = 10000  # Final money for completing all questions
        elif i == 9:
            money = 320000  # Final money for reaching the last question and answering correctly
    else:
        print("Wrong answer! Game over.\n")
        break

# When the loop ends (either by quitting or answering all questions)
print(f"Your total prize money is Rs. {money}")
