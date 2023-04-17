const sleep = ms => new Promise(r => setTimeout(r, ms));
uy = 10
dy = 70
stream = await navigator.mediaDevices.getDisplayMedia({
    video: {
        displaySurface: 'window',
        frameRate: 10,
        cursor: 'never'
    },
    audio: false
});
const track = stream.getVideoTracks()[0];
const imageCapture = new ImageCapture(track);

async function solve(x1) {
    x2 = x1+40;
    x3 = x2+40;
    for (i = 0; i < 27; i++) {
        for (j = 0; j < 27; j++) {
            for (k = 0; k < 27; k++) {
                document.elementFromPoint(x3, uy).click()
                const bitmap = await imageCapture.grabFrame()
                const canvas = document.getElementById("canv");
                canvas.height = 10;
                canvas.width = 10;
                const context = canvas.getContext('2d')
                context.drawImage(bitmap, -10, -70,bitmap.width, bitmap.height);
                if (context.getImageData(0,0,1,1).data[0] == 20) {
                    console.log("flag")
                    return;
                }
                // await sleep(100);
            }
            // reset
            for (k = 0; k < 27; k++) {
                document.elementFromPoint(x3, dy).click()
            }
            document.elementFromPoint(x2, uy).click()
        }
        for (j = 0; j < 27; j++) {
            // reset
            document.elementFromPoint(x2, dy).click()
        }
        document.elementFromPoint(x1, uy).click()
    }
}
// absolute x position of first of the 3 letters
solve(810)