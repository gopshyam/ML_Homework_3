#! /usr/bin/env python

import math

def split_data(data, feature_index):
    #returns two datasets which are classified based on the feature sets
    pos_set = list()
    neg_set = list()
    for element in data:
        if element[feature_index] == '1':
            pos_set.append(element)
        else:
            neg_set.append(element)

    return neg_set, pos_set

def find_entropy(data):
    #Finds entropy on a list of data based on the class values
    pos_count = 0

    for element in data:
        if element[-1] == '1':
            pos_count += 1 

    total_count = len(data)
    neg_count = total_count - pos_count

    p_pos = pos_count/float(total_count)
    p_neg = neg_count/float(total_count)
    
    if p_pos == 0 or p_neg == 0:
        return 0

    entropy = ( -1 * p_pos * math.log(p_pos)) + ( -1 * p_neg * math.log(p_neg))

    return entropy


def find_conditional_entropy(data, feature_index):
    #Finds the conditional entropy on the given dataset with all the features in the list of features
    neg_set, pos_set = split_data(data, feature_index)
    total_count = len(data)
    pos_count = len(pos_set)
    neg_count = len(neg_set)
    
    pos_entropy = find_entropy(pos_set)
    neg_entropy = find_entropy(neg_set)

    conditional_entropy = ( float(pos_count/total_count) * pos_entropy ) + ( float(neg_count/total_count) * neg_entropy )
    return conditional_entropy 



def main()
    with open("Data/data_sets1/training_set.csv", 'r') as f:
        raw_data = f.readlines()

    feature_labels = raw_data[0].strip().split(',')
    data = [x.strip().split(',') for x in raw_data[1:]] #Data contains all the training data

    remaining_features = feature_labels[:]

    nodes = list()
    impure_leaf_nodes = list()

    #Find the first node to split on
    conditional_entropy = 1
    split_feature_index = 0

    current_entropy = find_entropy(data)
    for feature in remaining_features:
        feature_index = feature_labels.index(feature)
        feature_conditional_entropy = find_conditional_entropy(data, feature_index)
        if feature_conditional_entropy < conditional_entropy:
            conditional_entropy = feature_conditional_entropy
            split_feature_index = feature_index
    
    split_feature_label = feature_labels[split_feature_index]
    remaining_features.remove(split_feature_label)

    neg_set, pos_set = split_data(data, split_feature_index) 
    class_prediction = None
    if (len(neg_set) == 0):
        class_prediction = 1
    if (len(pos_set) == 0):
        class_prediction = 0

    node = [split_feature_label, neg_set, pos_set, class_prediction]
    nodes.append(node)
    if (!is_pure):
        impure_leaf_nodes.append(node)
    #First node done

    while(leaf_nodes and remaining_features):
        pos_set, 



if __name__ == '__main__':
    main()
