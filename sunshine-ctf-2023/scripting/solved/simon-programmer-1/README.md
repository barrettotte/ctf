# simon-programmer-1

```js
console.log(global_frequencies)

// 30 frequencies
// 1st: frequencies[0:9]  (10)
// 2nd: frequencies[0:10] (11)
// 3rd: frequencies[0:11] (12)

const solve = () => {
    console.log('solving...');

    var x = 0;
    while (global_limit <= global_frequencies.length && x <= global_frequencies.length+5) {
        console.log(`global limit: ${global_limit}`);

        current_frequencies_used_global = [];
        const freqs = global_frequencies.slice(0, global_limit);

        for (var i = 0; i < freqs.length; i++) {
            let f = freqs[i].replace(/.*\/([-A-Za-z0-9_=]+).wav/, "$1")
            current_frequencies_used_global.push(f);
        }
        console.log(current_frequencies_used_global);
        
        if (!checkAnswer()) {
            console.log('FAILED!');
            break;
        }
        playSimon(global_limit + 1);

        x++;
    }
    console.log('done!');
};
// hit play once, then solve()
solve();
```

flag displays on page, forgot to copy/paste here before moving on
