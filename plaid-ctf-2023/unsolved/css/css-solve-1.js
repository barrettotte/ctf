const $$ = document.querySelectorAll.bind(document)
const positions = [...$$("[style*=\"background:url\"")].map((x) => (parseInt(atob(x.style.background.slice("url('data:image/svg+xml;base64,".length, -2)).split("540H0ZM")[1].split("V")[0].split(" ")[1]) - 2) / 20)
const necessaryPositions = (i) => +getComputedStyle($$("[style*=\"background:url\"")[i]).top.slice(0, -2) + -60 + 20 * positions[i]
const getSections = (i) => { const all = [...$$("[style*=\"position:absolute;top:0;\"][style*=\"font-size:0px;list-style:none\"]")[i].querySelectorAll(":last-child > details")]; return [all.slice(0, 26).reverse(), all.slice(26, 52).reverse(), all.slice(52).reverse()] }
const removeOpens = (vs) => vs.map((v) => v.removeAttribute("open"));
const bruteSegment = async (seg) => {
  const [as, bs, cs] = getSections(seg)
  for (let a = 0; a < 27; a ++) {
      for (let b = 0; b < 27; b ++) {
          for (let c = 0; c < 27; c ++) {
              const count = [0, 1, 2, 3].reduce((acc, i) => acc + (necessaryPositions(seg * 4 + i) === 0 ? 1 : 0), 0);
              if (count === 4) {
                  return;
              } else if (count > 1) {
                  console.log(a, b, c, count);
              }
              if (c !== 26) { cs[c].setAttribute("open", ""); } else { removeOpens(cs); }
          }
          if (b !== 26) { bs[b].setAttribute("open", ""); } else { removeOpens(bs); }
          await new Promise((resolve) => setTimeout(() => resolve(void 0), 0));
          if (window.STOP) { return }
      }
      if (a !== 26) { as[a].setAttribute("open", ""); } else { removeOpens(as); }
  }
}
const bruteAll = async () => { for (let i = 0; i < 13; i++) await bruteSegment(i); }
bruteAll()
