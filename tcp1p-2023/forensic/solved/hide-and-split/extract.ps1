$folderPath = "C:\Users\Barrett\Downloads\challenge"

# Get a list of all text files in the folder
$files = Get-ChildItem -Path $folderPath -Filter *.txt

# Loop through each text file and extract its alternate data stream
$blob=''
foreach ($file in $files) {
    Write-Host "$($file.FullName)"
    
    $streams = Get-Item -Path $file.FullName -Stream *

    foreach ($stream in $streams) {
        Write-Host "    Found stream $($stream.Stream)"
        if ($stream.Stream -ne ":`$DATA") {
            $extracted_stream = Get-Content -Path $file.FullName -Stream $stream.Stream
            Write-Host "    Extracted $($file.FullName):$($stream.Stream) ($($extracted_stream.Length) bytes)"
            $extracted_name = [System.IO.Path]::ChangeExtension($file.FullName, "") + $stream.Stream
            Set-Content -Path $extracted_name -Value $extracted_stream

            $blob += $extracted_stream
        }
    }
}

Set-Content -Path 'blob.txt' -Value $blob

# more < flag99.txt:flag99
# c49e448e448e448e4487faf7fd99fb41dd95101ee0000000049454e44ae426082
# cyberchef from hex -> PNG + IHDR

# 00
# 89504e470d0a1a0a0000000d49484452000003390000033908000000000179a0c500000e684
# another png IDHR
