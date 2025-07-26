famous_quote = "Há limites para aquilo que o  POVO  português pode aguentar."
##print(famous_quote.count("po"))
##print(famous_quote.lower())

#c)
f = famous_quote.replace("a", "_")
fa = f.replace("o", "*")
fam = fa.replace("_", "o")
famous = fam.replace("*", "a")
print(famous)

##print(f.replace("o", "a"))
##f = ""
##indice = 0
##for i in famous_quote: 
##    if i == "a":
##        f = f + "o"
##    elif i == "o":
##        f = f + "a"
##    else:
##        f = f + i
##print(f)


#d)
##print(famous_quote.split(" "))

#e)
#print(famous_quote.replace("  ", " "))
##for i in famous_quote:
##    if i == "u":
##        fa = famous_quote.split(i)
##    elif i == "t":
##        fa = famous_quote.split(i)
##print(fa)

#f)
##fam = ""
##for i in range(len(famous_quote)):
##    if i % 2 == 0:
##        fam = fam + "2"
##    else:
##        fam = fam + famous_quote[i]
##print(fam)
##x = "".join([famous_quote[x] if x%2 != 0 else "2" \
##     for x in range(len(famous_quote))])
##print(x)
