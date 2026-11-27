def main():
    answer = input("What is the Answer to the Great Question of Life, thhe Universe, and Everything? ").lower().strip()
    
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")
main()
