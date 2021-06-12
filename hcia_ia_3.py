instructions = """\nINSTRUCTIONS:
\t1. In the single choice questions: just type the corresponding letter. 
\t\tExample: type "A", not "A,".
\t2. In the multiple choice questions: your answer should be separated by "," and the letters should be in alphabetical order. 
\t\tExample: type "A,C,D", not "C,A,D".
\n
"""


def start_test(n_questions, questions_file):
	"""Start the Huawei HCIA 3.0 IA simulator.

    Keyword arguments:
    n_questions -- the number os questions of the test.
    questions_file -- the file that contatains the questions (in .txt format).
    """
	file = open("questions/"+questions_file, "r")
	c = 0
	correct = []
	wrong = []

	for i in range(3325):
		line = file.readline()
		
		if "Answer: " in line:
			c += 1
			if len(str(line[8:]).strip()) > 1:
				print("\nMultiple Choice")
			else:
				print("\nSingle Choice")
			answ = str(input("\nAnswer: ")).upper()
			if answ == str(line[8:]).strip():
				correct.append(c)
			else:
				wrong.append(c)
				print("Correct answer: ", str(line[8:]))
			print("\n","-"*10, "Correct: ", len(correct), "-"*10, "\n", "-"*10, "Wrong: ", len(wrong), "-"*10 )
			continue

		if c == n_questions:
			break
		print(line)

	dict_result = {"Corrects":correct,
					"Wrongs":wrong,
					"n_questions":n_questions}

	file.close()

	return dict_result

def show_result(dict_result):
	"""Start the Huawei HCIA 3.0 IA simulator.

    Keyword arguments:
    dict_result -- a python dictionary that contains the result of the test and the number of questions, 
    """

	corrects = dict_result["Corrects"]
	wrongs = dict_result["Wrongs"]
	n_questions = dict_result["n_questions"]

	print("\n\n","-"*10,"Final Result", "-"*10)

	final_note = (len(corrects)*100)/n_questions
	print("\nResult: ", final_note*10)

	if final_note*10 > 600:
		print("\nYOU PASS!")
	else:
		print("\nI'm sorry, you don't pass, but please try again!")

	if len(wrongs) > 0:
		print("\nSome questions for review:", end=" ")
		for i in wrongs:
			if i == wrongs[-1]:
				print(i)
			else:
				print(i, end=", ")
		
	    