attendee_names=[]


attendee_count=int(input("Attendee to add: "))

for x in range(attendee_count):
    attendee_name=input("Attendee name: ")
    attendee_names=attendee_names+[attendee_name]
print(attendee_names)
"""
attendee_name = input("Attendee name to remove: ")
if attendee_name in attendee_names:
    attendee_names.remove(attendee_name)
print(attendee_names)
"""

remove=attendee_names.pop(-1)
print(attendee_names)

print(remove)


