
# Created by admin on 9/1/17.

# Loop over all files in repo root
# uh, go up one...

# Add a listing for that file to a HTML page


import os

reponame = 'week2-examples-css-bootstrap'

out = "<html><head><title>Index</title></head><body><h2>" + reponame + "</h2>"

levelsdown = 0

basepath = "https://minneapolis-edu.github.io/" + reponame + "/"  #todo generate this? Read git config

end = "</body></html>"

entry = '<a href="%s">%s</a><br>'

ignore = ['.git', '.idea', 'index_builder', 'index.html', 'README.md']



def write_level(root):

    global levelsdown
    global out

    print(root)

    for f in os.scandir(root):

        if f.name in ignore:
            continue

        if f.is_dir():
            levelsdown +=1

            fname = ( levelsdown*"" ) + f.name

            out += "<h3>%s</h3>" % fname
            out += '\n'
            write_level(f.path)


        else:

            print(f.name)

            path = f.path.replace("../", "")

            link = basepath + path
            fname = ( levelsdown*"" ) + f.name
            html = entry % (link, fname)
            out += html
            out += '\n'

    levelsdown -=1


write_level("..")


out += end

with open('../index.html', 'w') as f:
    f.write(out)
    f.close()








