import hcia_ia_3

# Instructions
print(hcia_ia_3.instructions)

# Starting the test with 10 questions in the test_questions.txt file
result = hcia_ia_3.start_test(10, "test_questions.txt")

# Showing the result
hcia_ia_3.show_result(result)