# css

no js, but still incrementing characters...how?

42 char flag...

```
1 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 62V78H198V62Z"/></svg>
2 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 42V58H198V42Z"/></svg>
3 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 442V458H198V442Z"/></svg>
4 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 122V138H198V122Z"/></svg>
5 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 22V38H198V22Z"/></svg>
6 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 82V98H198V82Z"/></svg>
7 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 242V258H198V242Z"/></svg>
8 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 142V158H198V142Z"/></svg>
9 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 102V118H198V102Z"/></svg>
10 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 302V318H198V302Z"/></svg>
11 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 202V218H198V202Z"/></svg>
12 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 162V178H198V162Z"/></svg>
13 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 182V198H198V182Z"/></svg>
14 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 222V238H198V222Z"/></svg>
15 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 262V278H198V262Z"/></svg>
16 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 2V18H198V2Z"/></svg>
17 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 282V298H198V282Z"/></svg>
18 <svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 322V338H198V322Z"/></svg>
```

```html
<div style="position:absolute;top:calc(20 * (-9px + min(
max(100% - 0px, -27 * (100% - 0px)), max(100% - 26px, -27 * (100% - 26px)), max(100% - 143px, -27 * (100% - 143px)), max(100% - 78px, -27 * (100% - 78px)), max(100% - 39px, -27 * (100% - 39px)), max(100% - 52px, -27 * (100% - 52px)), max(100% - 104px, -27 * (100% - 104px)), max(100% - 13px, -27 * (100% - 13px)), max(100% - 91px, -27 * (100% - 91px)), max(100% - 130px, -27 * (100% - 130px)), max(100% - 156px, -27 * (100% - 156px)), max(100% - 65px, -27 * (100% - 65px)), max(100% - 117px, -27 * (100% - 117px))
)));width:200px;height:540px;background:url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iNTQwIj48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMCAwSDIwMFY1NDBIMFpNMiAxMjJWMTM4SDE5OFYxMjJaIi8+PC9zdmc+');user-select:none;pointer-events:none">
</div>
```

data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iNTQwIj48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMCAwSDIwMFY1NDBIMFpNMiAxMjJWMTM4SDE5OFYxMjJaIi8+PC9zdmc+
cyberchef it
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="540"><path fill="#fff" d="M0 0H200V540H0ZM2 122V138H198V122Z"/></svg>

on main div, ticked off overflow:hidden
letters grow downwards

tickers grouped into threes

42/3 = 14

26 <details> <div style="height:729px"></div>
26 <details> <div style="height:27px"></div>
26 <details> <div style="height:1px"></div>