function neuronExplanationButton() {
    let layer = document.querySelector('.input-layer');
    let index = document.querySelector('.input-index');
    executeButton(layer.value,index.value);
}

function keydownButton(key) {
    if (key === 'Enter') {
        neuronExplanationButton();
    }
}

function executeButton(layer,index) {
    let result_style = document.getElementsByClassName(".explanation-result");
    result_style.style = 'border: 1px solid lightgray;';
    
    let message = document.querySelector('.explanation-result');
    message = `<h4>EXPLANATION FOR LAYER: ${layer} AND INDEX: ${index}</h4>`
    if (layer === '0' && index === '0') {
        message += `<p>programming code structures and logic conditions.</p>`;
        message += `<h6>MOST FREQUENT TOKEN</h6>`
        message += `<div>
        <div class='token'>token "("</div>
        <div class='token'>token "if"</div>
        <div class='token'>token "null"</div>
        <div class='token'>token "!="</div>
        <div class='token'>token ")"</div>
        </div>`
        message += `<h6>MOST POSITIVE TOKENS</h6>`
        message += `<div>
        <div class='token'> token "account" : 2.75133276</div>
        <div class='token'>token "(" : 2.44138598</div>
        <div class='token'>token "Message" : 2.37940383</div>
        <div class='token'>token "found" : 2.35543394</div>
        <div class='token'>token "message" : 2.09572244</div>
        </div>`
        message += `<h6>MOST AVERAGE POSITIVE TOKENS</h6>`
        message += `<p><div>
        <div class='token'> token "Message" : 2.75133276</div>
        <div class='token'> token "(" : 1.921729908</div>
        <div class='token'> token "!" : 1.77485001</div>
        <div class='token'> token "..." : 1.52603793</div>
        <div class='token'> token "&&" : 1.2722299675</div>
        </div>`

    } else {
        message += `<p>Working on reading the neuron.</p>`;
    }
    document.querySelector('.explanation-result').innerHTML = message;
}

function neuronRandom() {
    layer = getRandomInt(7);
    index = getRandomInt(768);
    executeButton(layer,index);
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}