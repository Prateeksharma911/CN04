from ColorGame import ColorGame

if __name__ == "__main__":
    colorGameObj = ColorGame()
    print("Only way to exit is exit")
    print("Whats your command?")
    command=''
    while command!="exit":
        command = input()
        
        if command=='':
            pass

        else:
            results = colorGameObj.evalInput(command.lower().strip())

            if type(results)==list:
                for result in results:
                    print(result)

            else:
                print(results)

    print("Thanks for playing")
