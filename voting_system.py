names = []
userVote = int(input("enter how many voters : "))
for i in range(userVote):
    voter = input("who do you wanna vote for ? (markus , anderias): ").lower()
    names.append(voter)
if names.count("markus") > names.count("anderias"):
    print("the winnwe is Markus")
else:
    print("the winnwe is Anderias")