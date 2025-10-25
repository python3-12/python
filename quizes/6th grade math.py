import random

# List of questions and answers
questions = [
    {
        "question": "A submarine is 250 feet below sea level. What integer represents the submarine's depth?",
        "answer": "-250"
    },
    {
        "question": "What is the greatest common factor (GCF) of 18 and 24?",
        "answer": "6"
    },
    {
        "question": "Calculate: -15+7",
        "answer": "-8"
    },
    {
        "question": "If you have a fraction ⅝, what is its equivalent decimal?please answer with zero before point if answer is decimal with no whole number.",
        "answer": "0.625"
    },
    {
        "question": "What is the absolute value of -3.2?",
        "answer": "3.2"
    },
    {
        "question": "Simplify the ratio 12:18",
        "answer": "2:3"
    },
    {
        "question": "In a class, there are 15 boys and 12 girls. What is the ratio of boys to girls?",
        "answer": "15:12"
    },
    {
        "question": "A recipe calls for 2 cups of flour for every 3 cups of milk. If you use 9 cups of milk, how many cups of flour do you need",
        "answer": "6"
    },
    {
        "question": "What is 40 percent of 50?",
        "answer": "20"
    },
    {
        "question": "A jacket is 25 percent off. If the original price was $80, what is the sale price",
        "answer": "$60"
        
    },
    
    {
        "question": "Solve for x: 7x = 28",
        "answer": "4"
        
    },
    {
        "question": "solve for k: k-5 = 12",
        "answer": "17"
    },
    {
        "question": "What is the value of the expression 5+3×4",
        "answer": "17"
    },
    {
        "question": "A rectangular prism has a length of 5 inches, a width of 3 inches, and a height of 4 inches. What is its volume? answer with no space between the number and in",
        "answer": "60in"
    },
    {
        "question": "A square has a side length of 5 cm. What is its perimeter?",
        "answer": "20cm"
    },
    {
        "question": "Find the area of a rectangle with a length of 10 feet and a width of 6 feet.",
        "answer": "60ft"
    },
    {
        "question": "A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. What is the probability of drawing a red marble? (answer in decimal form)",
        "answer": "0.5"
    },
    {
        "question": "What is the mean (average) of the following data set: 10, 15, 20, 25?",
        "answer": "17.5"
    },
    {
        "question": "A school has 500 students. If 40 percent of the students are girls, how many girls are in the school?",
        "answer": "200"
    },
    {
        "question": "What is the range of the following data set: 10, 15, 20, 25?",
        "answer": "15"
    },
    {
        "question": "What is the mode of the following data set: 10, 15, 20, 25, 20?",
        "answer": "20"
    },
    {
        "question": "Add: 3/4+1/8",
        "answer": "7/8"
    },
    {
        "question": "Subtract: 5 - 2 1/3",
        "answer": "2 2/3"
    },
    {
        "question": "Multiply:  2/5×3/4 (please simplify and make proper)",
        "answer": "3/10"
    },
    {
        "question": "Divide: 4/5÷2/3 (please simplify and make proper)",
        "answer": "1 2/10"
    },
    {
        "question": "convert the fraction 3/5 into a persentage",
        "answer": "60%"
    },
    {
        "question": "A car travels 180 miles in 3 hours. What is its average speed in miles per hour?",
        "answer": "60mph"
    },
    {
        "question": "A recipe requires 3 cups of sugar for every 4 cups of flour. If you use 12 cups of flour, how much sugar do you need?",
        "answer": "9cups"
    },
    {
        "question": "On a map, 1 inch represents 50 miles. If two cities are 3.5 inches apart on the map, what is the actual distance between them?",
        "answer": "175mi"
    },
    {
        "question": "A bag contains 4 red marbles, 6 blue marbles, and 5 green marbles. What is the probability of randomly drawing a blue marble?",
        "answer": "0.4"
    },
    {
        "question": "Find the median of this data set: 12, 8, 15, 10, 11, 15",
        "answer": "11.5"
    },
    {
        "question": "A survey of 100 students found that 60 percent like pizza. How many students like pizza?",
        "answer": "60"
    }



]


# Shuffle the questions
random.shuffle(questions)

# Loop through each question
for question in questions:
    while True:
        user_answer = input(question["question"] + "\n").strip().lower()
        if user_answer == question["answer"]:
            print("Correct!")
            break
        else:
            print("Incorrect! Try again.")
