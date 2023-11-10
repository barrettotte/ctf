from pwn import *

io = process('./SpellBrewery')

correct_ingredients = [
    "Phantom Firefly Wing",
	"Ghastly Gourd",
	"Hocus Pocus Powder",
	"Spider Sling Silk",
	"Goblin's Gold",
	"Wraith's Tear",
	"Werewolf Whisker",
	"Ghoulish Goblet",
	"Cursed Skull",
	"Dragon's Scale Shimmer",
	"Raven Feather",
	"Dragon's Scale Shimmer",
	"Zombie Zest Zest",
	"Ghoulish Goblet",
	"Werewolf Whisker",
	"Cursed Skull",
	"Dragon's Scale Shimmer",
	"Haunted Hay Bale",
	"Wraith's Tear",
	"Zombie Zest Zest",
	"Serpent Scale",
	"Wraith's Tear",
	"Cursed Crypt Key",
	"Dragon's Scale Shimmer",
	"Salamander's Tail",
	"Raven Feather",
	"Wolfsbane",
	"Frankenstein's Lab Liquid",
	"Zombie Zest Zest",
	"Cursed Skull",
	"Ghoulish Goblet",
	"Dragon's Scale Shimmer",
	"Cursed Crypt Key",
	"Wraith's Tear",
	"Black Cat's Meow",
	"Wraith Whisper"
]

for i, ingredient in enumerate(correct_ingredients):
    print(io.recvuntil(b'> '))
    io.sendline(b'3')
    print(io.recvuntil(b'? '))
    io.sendline(ingredient.encode())

io.sendline(b'4')
io.interactive()
