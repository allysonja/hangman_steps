import requests

words = requests.get("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain").content.splitlines()
x = 0
# for w in words:
    # w = print(str(w).replace("b",""))
    # print(str(w).replace("\'",""))
    # print(w[1:-1])
    # x += 1

with open("dictionary.txt",'w') as file:
    for w in words:
        w = str(w).replace("b","")
        # w = str(w).replace("'","")
        file.write(w + "\n")