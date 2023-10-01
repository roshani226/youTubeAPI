import matplotlib.pyplot as plt

def calculate_accuracy(labeled_data):
    correct_predictions = sum(labeled_data['result'] == labeled_data['expected_result'])
    total_predictions = len(labeled_data)
    accuracy = correct_predictions / total_predictions * 100
    return accuracy

#def plot_accuracy(accuracy):
#    labels = ['Accuracy']
#    values = [accuracy]
#
#    plt.bar(labels, values)
#    plt.ylim([0, 100])  # Set the y-axis limit from 0 to 100
#    plt.ylabel('Accuracy (%)')
#    plt.title('Model Accuracy')
#    plt.show()
