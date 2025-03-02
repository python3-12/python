import random

# List of questions and answers
questions = [
    {
        "question": "What Pokémon is mostly dark blue with a yellow chest, has a white triangular marking over each eye, and has a light blue four-pointed star on each thigh, and yellow on the lower half of its face?",
        "answer": "greninja"
    },
    {
        "question": "What pokemon is yellow, a large mouse with a lightning bolt-shaped tail, and has red sacs on its cheek?",
        "answer": "pikachu"
    },
    {
        "question": "What Pokémon is a yellow Pokémon, resembling a duck or a bipedal platypus, and is a Water-type Pokémon but has psychic power?",
        "answer": "psyduck"
    },
    {
        "question": "what pokemon has brown eyes, big ears, and pink paw pads?",
        "answer": "eevee"
    },
    {
        "question": "what pokemon has a blue body with purple eyes, a light brown belly, a tough red-brown shell on its back, and has a long tail that curls into a spiral?",
        "answer": "squirtle"
    },
    {
        "question": "what pokemon has  four small fangs visible on its upper and lower jaws, and a cream underside and an expansive cream coloration on the sole of its foot?",
        "answer": "charmander"
    },
    {
        "question": "what pokemon is small, amphibian, and a plant Pokémon that move on all four legs?",
        "answer": "bulbasaur"
    },
    {
        "question": "what pokemon has the ability to control time?",
        "answer": "dialga"
    },
    {
        "question": "what pokemon has the power to control space, is a water and dragon type, and is weak to dragon and fairy tipe attacks?",
        "answer": "palkia"
    }
]

# Shuffle the questions
random.shuffle(questions)

# Loop through each question
for q in questions:
    while True:
        user_answer = input(q["question"] + " ").strip().lower()
        if user_answer == q["answer"]:
            print("Correct!")
            break
        else:
            print("Incorrect! Try again.")
