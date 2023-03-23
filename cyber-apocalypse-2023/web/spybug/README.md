# spybug

> As Pandora made her way through the ancient tombs, she received a message from her contact in the Intergalactic Ministry of Spies. 
> They had intercepted a communication from a rival treasure hunter who was working for the alien species. 
> The message contained information about a digital portal that leads to a software used for intercepting audio from the Ministry's communication channels. 
> Can you hack into the portal and take down the aliens counter-spying operation?

TODO: review writeup

https://mukarramkhalid.com/hack-the-box-cyber-apocalypse-2023-the-cursed-mission-writeups/#web---spybug

## Attempt

/agents/register	
identifier	"6e438dc2-04ad-4304-abeb-331e514ec931"
token	"158f1eee-9427-41ff-b539-f220d8cbf6ff"

```js
"/agents/upload/:identifier/:token",
  
    const filepath = path.join("./uploads/", req.file.filename);
    const buffer = fs.readFileSync(filepath).toString("hex");

    if (!buffer.match(/52494646[a-z0-9]{8}57415645/g)) {
      fs.unlinkSync(filepath);
      return res.sendStatus(400);
    }
    // rec.wave -> 1.4M

    // 52494646 -> RIFF
    // 57415645 -> WAVE
```

0x2F2A1600 -> 0.737 GiB

The header of a WAV (RIFF) file is 44 bytes long, and the last four bytes indicate the size of the data section.

`audio/wav` vs `audio/wave` ?

filetype --mime-type rec.wav
rec.wav: audio/x-wav

https://en.wikipedia.org/wiki/List_of_file_signatures

52 49 46 46 ?? ?? ?? ??
57 41 56 45

```js
// why is there js in the wave file?
*/="";alert(0);/*
```

```sh
curl http://localhost:1337/agents/register
# {"identifier":"1037f7d6-fa0e-4fc1-b1da-d49e5d085f33","token":"d14c8ab3-a940-4872-8ea1-45238f288acc"}

# https://gist.github.com/z11i/fdd874573fc4956c3ee3aad164eddbfe

# WORKED!
curl http://localhost:1337/agents/upload/1037f7d6-fa0e-4fc1-b1da-d49e5d085f33/d14c8ab3-a940-4872-8ea1-45238f288acc \
  -X POST \
  -H 'Content-Type: multipart/form-data' \
  -F 'recording=@/home/barrett/repos/ctf/cyber-apocalypse-2023/web/spybug/rec.wav;type=audio/wave'

curl http://localhost:1337/agents/upload/1037f7d6-fa0e-4fc1-b1da-d49e5d085f33/d14c8ab3-a940-4872-8ea1-45238f288acc \
  -X POST \
  -H 'Content-Type: multipart/form-data' \
  -F 'recording=@./rec.wav;type=audio/wave'

curl http://localhost:1337/agents/upload/1037f7d6-fa0e-4fc1-b1da-d49e5d085f33/d14c8ab3-a940-4872-8ea1-45238f288acc \
  -X POST \
  -H 'Content-Type: multipart/form-data' \
  -F 'recording=@./rec.wav;type=audio/wave;filename="../../../../test.wav"' # nope
```

I don't have the energy for this one. So here's a guess:

- admin -> adminbot.js goes to panel as admin
- has to be pug SSTI
- create agent with SSTI in parameters
- use ngrok to leak admin creds?
