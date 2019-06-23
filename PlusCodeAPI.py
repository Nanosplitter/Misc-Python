print("Table Name:")
tableName = input()
print("Values: Comma-seperated")
values = input().replace(" ", "").split(",")

#Create---------------------------------------
create = ""
for i in values:
    create += "\n\nif (empty($_POST['" + i.lower() + "']))\n{\n\t$errors['" + i.lower() + "'] = '" + i + " cannot be blank';\n}\nelse\n{\n\t$form" + i + " = trim($_POST['" + i.lower() + "']);\n}"

createSQL = "INSERT INTO " + tableName + "("
for i in values:
    createSQL += "[" + i + "], "
createSQL = createSQL[:len(createSQL) - 2]
createSQL += ")\n VALUES("
for i in values:
    createSQL += ":" + i + ", "
createSQL = createSQL[:len(createSQL) - 2]
createSQL += ")"

createFill = ""
for i in values:
    createFill += "\"" + i + "\" => $form" + i + ",\n"

createFill = createFill[:len(createFill) - 2]

create += "\n" + createSQL + "\n" + createFill

#Edit----------------------------------------

edit = create

editSQL = "UPDATE " + tableName + "\nSET "

for i in values:
    editSQL += "[" + i + "] = :" + i + ",\n"

editSQL = editSQL[:len(editSQL) - 2]

editFill = createFill

edit += "\n" + editSQL + "\n" + editFill


print("CREATE:\n" + create)
print("\nEDIT:\n" + edit)





