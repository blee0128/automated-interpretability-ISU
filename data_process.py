import json
import os

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
        
def main():
    """ 
        process every json file in a given folder and extract the tokens and activations from each file. Write the required information into a new json file
    """
    layer_index = 0
    neuron_index = 0
    dictionary = {"dataclass_name": "NeuronRecord", "neuron_id": {"dataclass_name": "NeuronId", "layer_index": layer_index, "neuron_index": neuron_index},"random_sample": []}

    for i in range(27402):
        print('reading {}.json file'.format(i))
        filepath = os.getcwd() + '/data/jsonFile/{}.json'.format(i)
        json_object = open_file(filepath)
        token, activation = extract_values(json_object,layer_index,neuron_index)
        tok_act_dict = {"dataclass_name": "ActivationRecord", "tokens": token, "activations": activation}
        dictionary["random_sample"].append(tok_act_dict)
    
    json_dict = json.dumps(dictionary)
    
    with open("data.json", "w") as outfile:
        outfile.write(json_dict)


if __name__ == '__main__':
    main()

