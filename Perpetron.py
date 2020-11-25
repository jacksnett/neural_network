import random
import numpy as np


class Perceptron:

    def __init__(self, point_arr):
        self.point_arr = point_arr
        self.weights = (np.random.rand(2) - 0.5)
        self.learning_rate = 0.1
        self.correct_count = 0
        self.incorrect_count = 0

    @staticmethod
    def sum_weighted_inputs(inputs, weights):
        weighted_input = 0

        for index in range(len(weights)):
            weighted_input += inputs[index] * weights[index]
        return weighted_input

    @staticmethod
    def activation(weighted_inputs_sum):
        if weighted_inputs_sum >= 0:
            return 1
        else:
            return -1

    def guess(self, inputs):
        weighted_inputs_sum = self.sum_weighted_inputs(inputs, self.weights)
        return self.activation(weighted_inputs_sum)

    def train(self):
        for curr_point in self.point_arr:
            inputs = [curr_point.x, curr_point.y]
            result = self.guess(inputs)
            curr_error = curr_point.label - result
            self.adjust_weights(curr_error, inputs)
            self.print_curr_result()

    def adjust_weights(self, curr_error, inputs):

        for index in range(len(self.weights)):
            self.weights[index] += curr_error * inputs[index] * self.learning_rate

    def print_curr_result(self):
        for point in self.point_arr:
            inputs = [point.x, point.y]
            result = self.guess(inputs)

            if result == point.label:
                self.correct_count += 1

            else:
                self.incorrect_count += 1

        print('correct count = %d' % self.correct_count)
        print('incorrect count = %d\n\n\n' % self.incorrect_count)
        self.correct_count = 0
        self.incorrect_count = 0
