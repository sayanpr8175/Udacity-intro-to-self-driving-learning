console.log('Setting up Simulator...');
const simFrameDiv = $('#simulator_frame').html('<iframe src="./index.html" width="100%" height="500" />');
setTimeout(() => {
    const simFrame = simFrameDiv.find('iframe');
    if (simFrame !== undefined) {
        window.simulatorWindow = simFrame[0].contentWindow;
        console.log('Acquired simulator window!');
    }
}, 1000);