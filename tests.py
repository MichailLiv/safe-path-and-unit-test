# Run with: `python -m unittest discover`

####################################################################
# A collection of tests for a solution to Mr Little Z problem      #
#                                                                  #
# Tests are for solution logic (due to time constrain)             #

#                                                                  #
# Testing performed using python's unit test package. Test names   #
# are intended to be self-explanatory but comments are provided    #
# for clarity.                                                     #
#                                                                  #
# Data for testing provided in the test_data folder of this        #
# directory.                                                       #
#                                                                  #
#####################################################################


import unittest
from Find_Max_Path import Graph
from dataclass import DataClass
import numpy as np


class TestLogic(unittest.TestCase):
    '''
    A set of tests for the logic behind our solution technique.
    '''

    def experiment(self,name_text_file):
        inputs = DataClass()
        #name_text_file = input()
        inputs.Read(str(name_text_file))

        # Initialize graph
        g = Graph()
        # Initialize nodes on the graph
        g.set_node_names(inputs.names)

        # This can be used to reduce computation to reduce the number of connected nodes that are defined, however it is preferred not to,
        # because the weight in the graph might be chosen to be defined differently
        # visited=[]

        for i in range(0, inputs.n + 2):
            for j in range(0, inputs.n + 2):

                # visited.append(i)
                if j != i:
                    calculate_risk = np.linalg.norm(inputs.input_information[str(i)] - inputs.input_information[str(j)])
                    # insert edge betweem two nodes along with the corresponding weight
                    g.insert_edge(calculate_risk, int(i), int(j))
                else:
                    continue

        return g.dijkstar_output(0)

    def test_provided_example(self):
        '''Test the solution for the data given with the task'''
        name_text_file = 'provided_example_1'
        output= self.experiment(name_text_file)


        self.assertEqual(
            output[0],
            ['0', '1', '2', '4'],
            'Output path of algorithm failed for the first provided example.'
        )

        self.assertEqual(
            output[1],
            2.0,
            'Output of maximum distance failed in algorithm  for the first provided example.'
        )

    def test_provided_example2(self):
        '''Test the solution for the data given with the task'''
        name_text_file = 'provided_example_2'
        output= self.experiment(name_text_file)


        self.assertEqual(
            output[0],
            ['0', '1', '2', '4'],
            'Output path of algorithm failed for the second provided example.'
        )

        self.assertEqual(
            output[1],
            1.73,
            'Output of maximum distance failed in algorithm  for the second provided example.'
        )

    def test_provided_pertubation(self):
        '''Test the solution for the case where a low cost node is added in the graph but it far from the goal'''
        name_text_file = 'pertubation'
        output= self.experiment(name_text_file)


        self.assertEqual(
            output[0],
            ['0', '1', '3', '4'],
            'Output path of algorithm failed for the pertubation example.'
        )

        self.assertEqual(
            output[1],
            1,
            'Output of maximum distance failed in algorithm  for the pertubation example.'
        )

    def test_provided_symmetric_cone(self):
        '''Test the solution for the case where the data are on a cone with earth at the center'''
        name_text_file = 'Circle'
        output= self.experiment(name_text_file)


        self.assertEqual(
            output[0],
            ['0', '6'],
            'Output path of algorithm failed for the cone example.'
        )

        self.assertEqual(
            output[1],
            1,
            'Output of maximum distance failed in algorithm  for the cone example.'
        )

    def test_provided_Zearth_is_Eearth(self):
        '''Test the solution for the case where Zearth is actually Earth'''
        name_text_file = 'Zearth_is_Eearth'
        output= self.experiment(name_text_file)


        self.assertEqual(
            output[0],
            ['0', '4'],
            'Output path of algorithm failed for the Zearth_is_Eearth example.'
        )

        self.assertEqual(
            output[1],
            0,
            'Output of maximum distance failed in algorithm for the Zearth_is_Eearth example.'
        )




if __name__ == '__main__':
    unittest.main(verbosity=True)
