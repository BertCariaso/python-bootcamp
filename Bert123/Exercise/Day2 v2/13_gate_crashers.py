invited={"Ana","Ben","Carlo","Dani"}
attended={"Ben","Carlo","Ely"}

print("Involved Members:")
print(invited | attended)

print("Absent:")
print(invited-attended)

print("Not enrolled but attended:")
print(attended - invited)

print("Attended properly:")
print(attended & invited)

