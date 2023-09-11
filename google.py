import os
google = input("Enter Your Search:")
link = "Link:" + "https://www.google.com/search?q=" + google + "&rlz=1C1GCEA_enIR1074IR1074&oq=" + google + "&aqs=chrome..69i57j35i39j46i199i465i512j46i512j0i512j46i512l2j0i512j46i512l2.560j0j7&sourceid=chrome&ie=UTF-8"
openorno = input("Open With Your Browser Or links Command:")
if openorno == "browser":
    print("Link: " + link)
if openorno == "links":
    os.system("links " + link)