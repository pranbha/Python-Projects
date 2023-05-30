import webbrowser

while True:
    option = input("Type Y to make a search and type N to exit: ")
    match option:
        case "Y":
            Search = input("Enter your search: ")
            webbrowser.open("https://www.google.com/search?q=" + Search)

        case "N":
            break

print("Thank you for browsing. \nBye!")