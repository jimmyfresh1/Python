function incrementCounter(element) {
    let currentCount = parseInt(element.innerText);
    currentCount +=1
    element.innerText = currentCount;
    sessionStorage.setItem('count', currentCount);
}

function log() {
    console.log("I'm here!")
}