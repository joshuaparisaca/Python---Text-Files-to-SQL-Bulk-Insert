j = open("addresses.txt", "r");

streets = [];
cities = [];
statezip = [];

for line in j: 
    print(line); # Will display the entire string of addresses.txt
    if ',' in line:
        cities.append(line.split(',')[0]); # Will save cities in a new List
        statezip.append(line.split(',')[1]); # Will save states in a new List
    else:
        streets.append(line); # Will save streets as a List 
j.close();


q = open("streets.txt", "w"); # New file is created
for w in streets: # Will loop through the entire streets List
    q.write(w); # Will write each line to the streets.txt
q.close();

k = open("cities.txt", "w") # New file is created
for w in cities: # Will loop through the entire cities List
    k.writelines(w + '\n'); # Will write each line to the cities.txt
k.close();


state = [];
zip = [];
l = open("states.txt", "w")
m = open("zip.txt", "w")
for w in statezip:
    state.append(w.split()[0]);
    l.writelines(w.split()[0] + '\n');

    zip.append(w.split()[1]);
    m.writelines(w.split()[1] + '\n');
l.close()
m.close();


email = open('emails.txt', 'r');
firstn = open('firstname.txt', 'r');
lastn = open('lastname.txt', 'r');
streeta = open('streets.txt', 'r');
citya = open('cities.txt', 'r');
statea = open('states.txt', 'r');
zipa = open('zip.txt', 'r');

bulkload = open('bulkload.txt', 'w')
for i in range(1,51):
    data2 = 'INSERT INTO people_table (email, firstname, lastname, street, city, state, zip) VALUES ("' + email.readline() + '","' + firstn.readline() +'","' + lastn.readline() + '","' + streeta.readline() + '","' + citya.readline() + '","' + statea.readline() +'","' + zipa.readline() + '");'
    bulkload.writelines("".join( data2.splitlines())+ '\n');
bulkload.close();

email.close();
firstn.close();
lastn.close();
streeta.close();
citya.close();
statea.close();
zipa.close();