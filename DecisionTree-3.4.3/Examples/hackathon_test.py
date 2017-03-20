#!/usr/bin/env python

##  construct_dt_and_classify_one_sample_case4.py

##  This example script is for purely nemeric features generated by the
##  TrainingDataGeneratorNumeric class using the information in the parameter file
##  param_numeric.txt The training data was generated by script
##  generate_training_data_numeric.py.

##  Now how we tell the module that the class labels are placed in column indexed 1
##  and that the features are in columns indexed 2 and 3 of the csv file.

##  Remember that column indexing of the csv file is zero-based.

import sys
sys.path.append("..")

import DecisionTree

training_datafile = "train2.csv"

dt = DecisionTree.DecisionTree( training_datafile = training_datafile,
                                csv_class_column_index = 10,
                                csv_columns_for_features = [1,2,3,4,5,6,7,8,9],
                                entropy_threshold = 0.01,
                                max_depth_desired = 10,
                                symbolic_to_numeric_cardinality_threshold = 10,
                                csv_cleanup_needed = 1,
                              )
dt.get_training_data()
dt.calculate_first_order_probabilities()
dt.calculate_class_priors()

#   UNCOMMENT THE FOLLOWING LINE if you would like to see the training
#   data that was read from the disk file:
#dt.show_training_data()

root_node = dt.construct_decision_tree_classifier()

#   UNCOMMENT THE FOLLOWING TWO LINES if you would like to see the decision
#   tree displayed in your terminal window:
print("\n\nThe Decision Tree:\n")
root_node.display_decision_tree("     ")


# test_sample  = ['gdp = 50.0',
#                 'return_on_invest = 45']
#
# # The rest of the script is for displaying the classification results:
#
# classification = dt.classify(root_node, test_sample)
# solution_path = classification['solution_path']
# del classification['solution_path']
# which_classes = list( classification.keys() )
# which_classes = sorted(which_classes, key=lambda x: classification[x], reverse=True)
# print("\nClassification:\n")
# print("     "  + str.ljust("class name", 30) + "probability")
# print("     ----------                    -----------")
# for which_class in which_classes:
#     if which_class is not 'solution_path':
#         print("     "  + str.ljust(which_class, 30) +  str(classification[which_class]))
#
# print("\nSolution path in the decision tree: " + str(solution_path))
# print("\nNumber of nodes created: " + str(root_node.how_many_nodes()))

