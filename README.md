# Automated interpretability

## Code and tools

This repository contains code and tools associated with the [Language models can explain neurons in
language models](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html) paper, specifically:

* Code for automatically generating, simulating, and scoring explanations of neuron behavior using
the methodology described in the paper. See the
[neuron-explainer README](neuron-explainer/README.md) for more information.

Note: if you run into errors of the form "Error: Could not find any credentials that grant access to storage account: 'openaipublic' and container: 'neuron-explainer'"." you might be able to fix this by signing up for an azure account and specifying the credentials as described in the error message. 

* A tool for viewing neuron activations and explanations, accessible
[here](https://openaipublic.blob.core.windows.net/neuron-explainer/neuron-viewer/index.html). See
the [neuron-viewer README](neuron-viewer/README.md) for more information.

## Updated Resources

data_process.py: This python file converts the activation records from neurox for source code into the activation records needed by OpenAI for neuron explanation

data folder:
    newdata.json: dataset that was process and created from data_process.py for openAI API input

neuron-explainer:
    - generate_and_score_explanation.ipynb: updated the file to get explanation from openAI for our dataset
    - activations.py: added a function mod_load_neuron() to load neuron to the LLM

## Project
It reads data from sample [input](/automated-interpretability-ISU/data/newdata.json) file
- filepath to the neurox activations = filepath
- first digit = layer index
- second digit = neuron index 

This will provide explanation on the activation record.
```bash
python3 data_process.py 0 0 filepath
```