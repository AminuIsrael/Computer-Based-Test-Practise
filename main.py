print("-----------------------------------------------------------------------")
print("            Test your Knowledge on a particular subject/course")
print("                       Subject/Course: Physics")
print("                       Number of questions: 15")
print("                       Expected time: 10mins")
print("-----------------------------------------------------------------------\n")


class MCQ():  # Creating the object MCQ()
    def __init__(self, questions, answers):  # Creating object attributes for MCQ()
        self.questions = questions
        self.answers = answers


question = [  # This is a physics multiple choice questions I got from the web
    "\n1. Radiocarbon is produced in the atmosphere as a result of \n (a) collision between fast neutrons and nitrogen nuclei present in the atmosphere\n (b) action of ultraviolet light from the sun on atmospheric oxygen\n (c) action of solar radiations particularly cosmic rays on carbon dioxide present in the atmosphere\n (d) lightning discharge in atmosphere\n",
    "2. It is easier to roll a stone up a sloping road than to lift it vertical upwards because? \n (a) work done in rolling is more than in lifting\n (b) work done in lifting the stone is equal to rolling it\n (c) work done in both is same but the rate of doing work is less in rolling\n (d) work done in rolling a stone is less than in lifting it\n",
    "3. The absorption of ink by blotting paper involves \n (a) viscosity of ink\n (b) capillary action phenomenon\n (c) diffusion of ink through the blotting\n (d) siphon action\n",
    "4. Large transformers, when used for some time, become very hot and are cooled by circulating oil. The heating of the transformer is due to \n (a) the heating effect of current alone\n (b) hysteresis loss alone\n (c) both the heating effect of current and hysteresis loss\n (d) intense sunlight at noon\n",
    "5. Nuclear sizes are expressed in a unit named \n (a) Fermi\n (b) angstrom\n (c) newton\n (d) tesla\n",
    "6. Light year is a unit of \n (a) time\n (b) distance\n (c) light\n (d) intensity of light\n",
    "7. Mirage is due to \n (a) unequal heating of different parts of the atmosphere\n (b) magnetic disturbances in the atmosphere\n (c) depletion of ozone layer in the atmosphere\n (d) equal heating of different parts of the atmosphere\n",
    "8. Light from the Sun reaches us in nearly \n (a) 2 minutes\n (b) 4 minutes\n (c) 8 minutes\n (d) 16 minutes\n",
    "9. Stars appears to move from east to west because \n (a) all stars move from east to west\n (b) the earth rotates from west to east\n (c) the earth rotates from east to west\n (d) the background of the stars moves from west to east\n",
    "10. Pa(Pascal) is the unit for \n (a) thrust\n (b) pressure\n (c) frequency\n (d) conductivity\n",
    "11. Planets do not twinkle because \n (a) they emit light of a constant intensity\n (b) their distance from the earth does not change with time\n (c) they are very far away from the earth resulting in decrease in intensity of light\n (d) they are nearer to earth and hence we receive a greater amount of light and, therefore minor variations in the intensity are not noticeable\n",
    "12. Metals are good conductors of electricity because \n (a) they contain free electrons\n (b) the atoms are lightly packed\n (c) they have high melting point\n (d) All of the above\n",
    "13. If two bodies of different masses, initially at rest, are acted upon by the same force for the same time, then the both bodies acquire the same \n (a) velocity\n (b) momentum\n (c) acceleration\n (d) kinetic energy\n",
    "14. Pick out the scalar quantity \n (a) force\n (b) pressure\n (c) velocity\n (d) acceleration\n",
    "15.Rectifiers are used to convert \n (a) Direct current to Alternating current\n (b) Alternating current to Direct current\n (c) high voltage to low voltage\n (d) low voltage to high voltage\n",

]
data = [MCQ(question[0], "a"),  # Calling the object function and passing it to a list
        MCQ(question[1], "d"),
        MCQ(question[2], "b"),
        MCQ(question[3], "c"),
        MCQ(question[4], "b"),
        MCQ(question[5], "b"),
        MCQ(question[6], "a"),
        MCQ(question[7], "c"),
        MCQ(question[8], "b"),
        MCQ(question[9], "b"),
        MCQ(question[10], "d"),
        MCQ(question[11], "a"),
        MCQ(question[12], "b"),
        MCQ(question[13], "b"),
        MCQ(question[14], "b")
        ]


def Test(value):  # Creating a function for the test
    import time
    score = 0
    time_1 = time.time()
    while time_1 == time.time():
        for question in value:  # for loop to iterate over the questions
            print(question.questions)
            answer = (input("Choose option (a,b,c,d): ")).lower()
            if answer == question.answers:
                print("\nCorrect!\n")
                score += 1
            elif answer.isdigit():
                print("Wrong input, Choose option between(a,b,c,d)")
            else:
                print("\nWrong answer")
                print(f"The correct option is {question.answers}\n")
        time_spent = time.time() - time_1
        time_spent_tomin = (time_spent/60)
        time_spent_tomin2dp = "%.2f" % time_spent_tomin
    print(f"\nYour Score is {str(score)}/{str(len(data))}")
    print(f"You spent {time_spent_tomin2dp} minutes on the test")
    time.sleep(60*5)


Begin_test = (input("Begin test[y/n]:")).lower()

if Begin_test == "y" or Begin_test == "yes":
    Test(data)
elif Begin_test == "n" or Begin_test=="no":
    print("Okay")
else:
    print("Invalid Parameter")
