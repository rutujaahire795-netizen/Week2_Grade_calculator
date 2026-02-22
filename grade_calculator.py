# Student Grade Calculator - Compact Version
students, subjects = [], ["Math", "Science", "English"]

def get_grade(avg):
    return 'A' if avg >= 80 else 'B' if avg >= 70 else 'C' if avg >= 60 else 'D' if avg >= 50 else 'F'

def get_comment(grade, avg):
    comments = {'A': f"Excellent! {avg:.1f}%", 'B': f"Good! {avg:.1f}%", 'C': f"Fair! {avg:.1f}%", 
                'D': f"Passing! {avg:.1f}%", 'F': f"Failed! {avg:.1f}%"}
    return comments.get(grade, "")

# Input validation
num = 0
while num <= 0:
    try:
        num = int(input("Number of students: "))
    except:
        print("Invalid input!")

# Collect data
for i in range(num):
    name = input(f"\nStudent {i+1} name: ")
    marks = []
    for subject in subjects:
        mark = -1
        while mark < 0 or mark > 100:
            try:
                mark = float(input(f"{subject} marks: "))
            except:
                print("Enter 0-100!")
        marks.append(mark)
    
    avg = sum(marks)/len(marks)
    grade = get_grade(avg)
    students.append([name, marks, avg, grade, get_comment(grade, avg)])

# Display results
print("\n" + "="*50)
print(f"{'Name':<10} {'Avg':<6} {'Grade':<6} Comment")
print("-"*50)
for s in students:
    print(f"{s[0]:<10} {s[2]:<6.1f} {s[3]:<6} {s[4]}")

# Statistics
if students:
    averages = [s[2] for s in students]
    print(f"\n📊 Class Average: {sum(averages)/len(averages):.1f}%")
    print(f"🏆 Highest: {max(averages):.1f}% ({students[averages.index(max(averages))][0]})")
    print(f"📉 Lowest: {min(averages):.1f}% ({students[averages.index(min(averages))][0]})")
    
    # Save to file
    with open("results.txt", "w") as f:
        for s in students:
            f.write(f"{s[0]}: {s[2]:.1f}% - {s[3]}\n")
    print("✅ Results saved to results.txt")