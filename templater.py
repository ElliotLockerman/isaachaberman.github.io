#! /usr/bin/env python

import os
import sys
import copy

DEFAULT_TITLE = "Isaac Haberman"

def template(root):

    with open("components/head.html") as f:
        head = ["<!DOCTYPE html>", "<head>"] + f.readlines()

    with open("components/header.html") as f:
        header = f.readlines()

    with open("components/footer.html") as f:
        footer = f.readlines()


    for dirname, subdirlist, filelist in os.walk(root):
        for file in filelist:
            if file.find("-template.html") > 0:

                inpath = os.path.join(dirname,file)
                with open(inpath) as f:
                    contents = f.readlines()

                page_head = copy.copy(head)
                title_path = os.path.join(dirname, file.replace("-template", "-title"))
                if os.path.exists(title_path):
                    with open(title_path) as f:
                        title = f.readline()    
                else:
                    title = DEFAULT_TITLE

                page_head.append("<title>" + title + "</title>")


                css_file = file.replace("-template.html", ".css")
                css_path = os.path.join(dirname, css_file)
                if(os.path.exists(css_path)):
                    page_head.append("<link rel=\"stylesheet\" href=\"" + css_file + "\">")

                page_head.append("</head>")


                data = page_head + header + contents + footer

                outpath = os.path.join(dirname, file.replace("-template", ""))
                with open(outpath, "w") as f:
                    f.writelines(data)



if __name__ == "__main__":
    template(".")