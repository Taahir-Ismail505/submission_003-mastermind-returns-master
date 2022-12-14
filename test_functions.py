import unittest
from unittest.mock import patch
from mastermind import create_code ,check_correctness,answer_input ,take_turn
from io import StringIO

def get_answer_input():
    return input('Enter your guess: ') 

class MyTestCase(unittest.TestCase):

    def test_create_code(self):
        code = create_code()
        for i in  range(100) :
            self.assertEqual(type(code), list)
            self.assertEqual(len(code), 4)
            for j in range(4) :
                self.assertTrue(0 < code[j] <= 8)

    def test_check_correctness(self):
        turns =12 
        correct_digits_and_position = 4
        correct = bool(correct_digits_and_position)
        correct = check_correctness(turns,correct_digits_and_position)
        self.assertEqual(turns,12)
        self.assertTrue(correct)
    
    @patch("sys.stdin", StringIO("3728\n6342\n"))
    def test_answerinput(self):
        answer = get_answer_input()
        if len(answer) != 4:
            self.assertEqual(get_answer_input(), "3728")
            self.assertEqual(get_answer_input(), "6342")


    def test_take_turn(self):
        self.assertEqual(take_turn([4,5,6,7],[4,5,6,7]),(4,0))
        self.assertEqual(take_turn([4,5,6,7],[5,6,7,4]),(0,4))
        self.assertEqual(take_turn([1,2,3,8],[5,6,7,4]),(0,0))
        self.assertEqual(take_turn([4,5,6,7],[4,5,7,6]),(2,2))

            



if __name__ == '__main__':
    unittest.main()
