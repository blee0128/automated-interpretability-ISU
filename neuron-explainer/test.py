import json
import urllib.request

def load_az_json(url):
    with urllib.request.urlopen(url) as f:
        neuron_record = f.read()    

    return json.loads(neuron_record)
    
def load_neuron(layer_index, neuron_index):
    url = f"https://openaipublic.blob.core.windows.net/neuron-explainer/data/explanations/{layer_index}/{neuron_index}.json"

    return load_az_json(url)

# program entry point
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Load neuron explanation from Azure')
    parser.add_argument('layer_index', type=int, help='layer index')
    parser.add_argument('neuron_index', type=int, help='neuron index')
    args = parser.parse_args()

    neuron = load_neuron(args.layer_index, args.neuron_index)

    explanation = neuron["scored_explanations"][0]["explanation"]
    score       = neuron["scored_explanations"][0]["scored_simulation"]["ev_correlation_score"]

    print(f"Layer {args.layer_index}, Neuron {args.neuron_index}: [{explanation}] with score [{round(score, 2)}]")