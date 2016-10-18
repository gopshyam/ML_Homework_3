import pickle

from id3_predict import find_error

root_node = None

def find_optimal_node(current_node, data, feature_labels, root_node):
    if (current_node.is_pure):
        return

    if (current_node.left_node != None):
        find_optimal_node(current_node.left_node, data, feature_labels, root_node)

    if (current_node.right_node != None):
        find_optimal_node(current_node.right_node, data, feature_labels, root_node)

    current_error = find_error(data, root_node, feature_labels)

    current_node.is_pure = True

    new_error = find_error(data, root_node, feature_labels)

    if (new_error <= current_error):
        return

    current_node.is_pure = False

    
def main(n):
    with open('root_node' + str(n), 'r') as f:
        root_node = pickle.load(f)

    raw_data = []
    with open('Data/data_sets' + str(n) + '/validation_set.csv', 'r') as f:
        raw_data = f.readlines()

    feature_labels = raw_data[0].strip().split(',')[:-1]

    data = [x.strip().split(',') for x in raw_data[1:]]
    
    find_optimal_node(root_node, data, feature_labels, root_node)

    with open('pruned_root_node' + str(n), 'w') as f: 
        pickle.dump(root_node, f)


if __name__ == '__main__':
    main(1)
    main(2)
