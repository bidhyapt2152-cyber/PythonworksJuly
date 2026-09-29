#write

f = open("k.txt", "w")

# f.write("hello\n")
# f.write("python\n")
#f.write("""Although most people consider piranhas to be quite dangerous, they are, for the most part, entirely harmless. Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants. When confronted with humans, piranhas first instinct is to flee, not attack. Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas. If the fish are well-fed, they won t bite humans.""")
f.write("""Although most people consider piranhas to be quite dangerous,
Like sharks, snakes, and spiders, pirahnas are widely feared. Although 
most people consider piranhas to be quite dangerous, they are, for the
 most part, entirely harmless. Piranhas rarely feed on large animals; 
 they eat smaller fish and aquatic plants. When confronted with humans, 
 piranhas’ first instinct is to flee, not attack. Their fear of humans 
 makes sense. Far more piranhas are eaten by people than people are 
 eaten by piranhas. If the fish are well-fed, they won’t bite humans.
they are, for the most part, entirely harmless. Piranhas rarely feed
on large animals; they eat smaller fish and aquatic plants. When confronted with 
humans, piranhas first instinct is to flee, not attack. Their fear of 
humans makes sense. Far more piranhas are eaten by people than people 
are eaten by piranhas. If the fish are well-fed, they won't bite humans .""")

f.close()


#Read
f = open("k.txt", "r")
s = f.read()
print(s)
print(type(s))
f.close()