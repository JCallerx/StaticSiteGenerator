from textnode import *
from website_funcs import *
from generator_func import *
import sys

def main():
    copy_static("static", "docs")
    arguments = sys.argv
    if len(arguments) == 1:
        basepath = "/"
    else:
        basepath = arguments[1]
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)



if __name__ == "__main__":
    main()