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
        "question": "what pokemon is small, amphibian, and the first pokemon in the pokedex?",
        "answer": "bulbasaur"
    },
    {
        "question": "what pokemon has the ability to control time?",
        "answer": "dialga"
    },
    {
        "question": "what pokemon has the power to control space, is a water and dragon type, and is weak to dragon and fairy tipe attacks?",
        "answer": "palkia"
    },
    {
        "question": "what pokemon is a  large, dragon-like Pokémon, has two large wings with teal undersides and a flame burning at the tip of its tail?",
        "answer": "charizard"
        
    },
    
    {
        "question": "what pokemon has whiskers, black-and-brown ears, and a curled tail?",
        "answer": "meowth"
        
    },
    {
        "question": "what pokemon is constantly sleeping?",
        "answer": "snorlax"
    },
    {
        "question": "what pokemon has a rocky head and body, strong arms, and the ability to camouflage itself as a rock?",
        "answer": "geodude"
    },
    {
        "question": "what pokemon has a hardened, rock-like exterior and has an ability to roll into a ball and move at high speeds?",
        "answer": "golem"
    },
    {
        "question": "what pokemon has six tails and is a fox-like Pokémon with reddish-brown fur?",
        "answer": "vulpix"
    },
    {
        "question": "what pokemon is round with spikes on its back, is a ghost and poison type and is very mischievous?",
        "answer": "gengar"
    },
    {
        "question": "what pokemon has an appearance that combines traits of tigers and lions, with orange fur, black stripes, and cream-colored tufts?",
        "answer": "arcanine"
    },
    {
        "question": "what pokemon has blue fur, black appendages on its head, and a canine-like appearance?",
        "answer": "lucario"
    },
    {
        "question": "what pokemon is a large, orange-skinned Pokémon with a friendly, dragon-like appearance",
        "answer": "dragonite"
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
