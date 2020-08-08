humans = {
        "John": [25,"Male"],
        "Lisa": [25,"Female"],
        "Linda": [25,"Female",["Susan",6,"Female"]],
        "Michael": [25,"Male",["Karen",25,"Female"],["Greg",7,"Male"]],
    }

print(humans["Linda"][2])
print(humans["Michael"][2][0],humans["Michael"][3][0])





