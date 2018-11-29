import bandCount

def main():
    while True:
        choice = input("Hello, what would you like to count by? Type \"help\" for all options.")
        if choice == "leave":
            print("Goodbye!")
            break
        elif choice == "help":
            print("The choices are:\n\"leave\"\n\"country\"\n\"alphabet\"\n\"genre\"")
        elif choice == "country":
            bandCount.countBands("country", "bandListCountry_info")
        elif choice == "alphabet":
            bandCount.countBands("alphabet", "bandListAlpha_info")
        elif choice == "genre":
            bandCount.countBands("genre", "bandListGenre_info")
        else:
            print("Not a valid choice")
    
if __name__ == "__main__":
    main()
    exit()