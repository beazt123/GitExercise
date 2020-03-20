#Student chooses 4H2 or 3H2 + 1H1 subject
#Enter rank points of each subject without entering the subject title
#For 4H2, the calculator automatically selects the worst H2 subject to be converted to a H1 grade, before totaling the pts
#For 3H2 + 1H1, the calc will total up the pts
#H2: A:20, B:17.5, C:15, D:12.5, E:10, S=5, U=0
#H1: A:10, B:8.75, C:7.5, D:6.25, E:5, S:2.5, U=0

print("                    _____             _____             _____                              _____    _____                _______       ")
print("      /|   |       |       |       | |       |         |     \       /| |\      | |   /   |     \  /     \  |  |\      |    |")
print("     / |   |       |       |       | |       |         |     |      / | | \     | |  /    |     | |      |  |  | \     |    |")
print("    /  |   |       |       |       | |       |         |     |     /  | |  \    | | /     |     | |      |  |  |  \    |    |")
print("   /___|   |       |_____  \       / |_____  |         |_____/    /___| |   \   | |/      |_____/ |      |  |  |   \   |    |")
print("  /    |   |       |        \     /  |       |         |     \   /    | |    \  | |\      |       |      |  |  |    \  |    |")
print(" /     |   |       |         \   /   |       |         |      | /     | |     \ | | \     |       |      |  |  |     \ |    |")
print("/      |   |______ |_____     \_/    |_____  |_____    |      |/      | |      \| |  \    |        \_____/  |  |      \|    |")

print("Congratulations on receiving your A level results! \n I can help you calculate your rank points out of 90.")
print("How many H2 subjects did you take?")
correct_number = False
while correct_number == False:
	no_of_H2 = int(input("Number of H2 Subjects: "))
	if no_of_H2 != 3 and no_of_H2 != 4:
		print("I don't think you studied in Singapore. Pls look for a calculator that is based in your own country.")
		correct_number = False
	else:
		correct_number = True
	

H2_subjects = {}
H1_subjects = {}
H2 = {"A":20, "B":17.5, "C":15, "D":12.5, "E":10, "S":5, "U":0}
H1 = {"A":10, "B":8.75, "C":7.5, "D":6.25, "E":5, "S":2.5, "U":0}
print("Pls enter the name of your H2 subject one by one.")
for i in range(no_of_H2): #Collects the name of subject and the correspoonding grade and puts them in a dictionary
	each_subject = input("Name of H2 subject: ")
	grade = input("Pls enter the grade you got for " + each_subject + "\nGrade: ")
	H2_subjects[each_subject] = grade.upper()
		
	
#Collect grades for the H1 subjects
GP = input("Enter your grade for GP\nGrade: ")
PW = input("Enter your grade for PW\nGrade: ")
H1_subjects["GP"] = GP.upper()
H1_subjects["PW"] = PW.upper()

#Takes in a dictionary of subjects and grades and returns a list of scores for those subjects
def grade_converter(subjectDict,refDict):
	scores = []
	for name, grade in subjectDict.items():
		scores.append(refDict[grade])
	return scores

H2_scores = grade_converter(H2_subjects,H2)

#Converts the worst H2 grade to a H1 grade if the person took 4 H2 subjects
if no_of_H2 == 4:
	extra_qn = False
	for key,value in H2.items():
		if min(H2_scores) == value: #Find the corresponding H2 grade
			print(value)
			H2_scores.remove(value) #Change the H2 grade
			H2_scores.append(H1[key])#to a H1 grade
#If the person took 3 H2 subjects, ask him to enter the name and grade of the H1 subject
elif no_of_H2 == 3:
	extra_qn = True
	
#If the person didn't take 4 H2s, he'll enter his H1 subject manually
while extra_qn == True:			
	remaining_H1 = input("Please enter the name of your last H1 subject.\nName of subject: ")
	H = remaining_H1[0].upper() + remaining_H1[1:].lower()
	remaining_H1_grade = input("Pls enter the grade you got for " + H + "\nGrade: ")
	H1_subjects[H] = remaining_H1_grade.upper()
	break

#After all the H1 subjects have been entered, calculate the total score
H1_scores = grade_converter(H1_subjects,H1)
	
#Sums up the total scores from both H1 subjects and H2 subjects	
def total_score(list):
	x = 0.0
	for item in list:
		x += item
	return x

#Calculate the total score composing of the H1 & H2 subjects
rank_points = total_score(H1_scores) + total_score(H2_scores)

#Return the user a results slip comprising of all his grades and a rank point score out of 90
print("\n")
print("_______________________________")
print("\n")
print("A level results slip")
print("\n")
for key,value in H2_subjects.items():
	print(key[0].upper() + key[1:].lower() + ": " + value)
for key,value in H1_subjects.items():
	print(key + ": " + value)
print("\n")
print(str(rank_points) + "/90")
	
		



