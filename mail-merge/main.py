# Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

invited_names = []
with open("./Input/Names/invited_names.txt") as file:
    for name in file.readlines():
        invited_names.append(name.strip())

#In the starting_letter.txt replace the string [name] to the invited names
with open("./Input/Letters/starting_letter.txt") as file_2:
    content = file_2.read()
    for name in invited_names:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode= "x") as file_3:
            updated_letter = content.replace("[name]", name)
            file_3.write(updated_letter)




