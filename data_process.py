import json
import os
import random
import sys

"""
    data_process.py converts the neuron activation from neurox format to openAI automated-interpretability format
"""

def open_file(filepath):
    """open file and convert to json format

        Args:
            filepath: filepath of the activation format

        Returns:
            json dictionary  
    """
    f = open(filepath)
    data = json.load(f)
    json_object = json.loads(data)['features']
    f.close()
    return json_object


def extract_values(json_dict,layer,neuronIndex):
    """ extract the tokens and activations from the given json dictionary based on the layer number and neuron index number

        Args:
            json_dict: json dictionary
            layer: layer number to extract
            neuronIndex: neuronIndex number to extract

        Returns:
            tokens: list
            activations: list 
    """
    tokens = []
    activations = []
    
    for tok in json_dict:
        text = tok['token']
        cleaned_text = text.replace("Ġ","")
        final_text = cleaned_text.replace("'","")
        tokens.append(final_text)
        activations.append(tok['layers'][layer]['values'][neuronIndex])

    return tokens, activations

def split_most_positive_activation_record(list):
    """ split the list of activation tokens into random and most_positive_activation samples

        Args:
            list: list of all the activations records

        Returns:
            random_sample: list
            most_positive_activations: list 
    """
    random_sample = []
    most_positive_activation_records = []
    average = []
    for act in list:
        avg = sum(act['activations']) / len(act['activations'])
        average.append(avg)
    average.sort()
    count = len(average) - 50
    min = average[count]
    for act in list:
        avg = sum(act['activations']) / len(act['activations'])
        if avg >= min:
            most_positive_activation_records.append(act)
        else:
            random_sample.append(act)
    
    while len(random_sample) > 50:
        random_sample.pop(random.randrange(len(random_sample)))

    return random_sample, most_positive_activation_records



def main():
    """ 
        process every json file in a given folder and extract the tokens and activations from each file. Write the required information into a new json file
    """

    # Boolean to be set if valid flag is entered
    argument_parsed = False

    if len(sys.argv) >= 3:
        file_path = sys.argv[1]
        layer_index = sys.argv[2]
        neuron_index = sys.argv[3]
        argument_parsed = True

    # Print usage if argument is not parsed
    if not(argument_parsed):
        print("Usage:")
        print("\t\tpython data_process.py layer_index neuron_index filepath")
        sys.exit(0)


    print('layer_index: {}'.format(layer_index))
    print('neuron_index: {}'.format(neuron_index))
    dictionary = {"dataclass_name": "NeuronRecord", "neuron_id": {"dataclass_name": "NeuronId", "layer_index": layer_index, "neuron_index": neuron_index}}
    res = []

    for i in range(27402):
        print('reading {}.json file'.format(i))
        neuroxfilepath = file_path + '/{}.json'.format(i)
        json_object = open_file(neuroxfilepath)
        token, activation = extract_values(json_object,layer_index,neuron_index)
        tok_act_dict = {"dataclass_name": "ActivationRecord", "tokens": token, "activations": activation}
        res.append(tok_act_dict)
    
    random_sample, most_positive_activation_records = split_most_positive_activation_record(res)
    dictionary["random_sample"] = random_sample
    dictionary["most_positive_activation_records"]= most_positive_activation_records
    
    json_dict = json.dumps(dictionary)
    
    with open("newdata.json", "w") as outfile:
        outfile.write(json_dict)


if __name__ == '__main__':
    main()

