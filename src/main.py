from textnode import *
from website_funcs import *
from generator_func import *
def main():
    copy_static("static", "public")
    generate_pages_recursive("./content", "./template.html", "./public")



if __name__ == "__main__":
    main()