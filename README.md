# Simulator for the Huawei HCIA IA 3.0 Certification

This repository was made to help with the studies for the certification. 

Using 6 diferents .txt file with 60 questions, you can test you knowleghe for the certification in this python program.

## Questions 

There are 7 files in this folder, each one have 60 questions (exept for the "test_questions.txt", this one have 10) with different questions.

## Example:

'''

import hcia_ia_3

# Instructions
print(hcia_ia_3.instructions)

# Starting the test with 10 questions in the test_questions.txt file
result = hcia_ia_3.start_test(10, "test_questions.txt")

# Showing the result
hcia_ia_3.show_result(result)

'''

