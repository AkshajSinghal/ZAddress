#Input: 1600 Amphitheatre Parkway, Mountain View, CA 94043

#Street: 1600 Amphitheatre Parkway
#City: Mountain View
#State: CA
#ZIP: 94043

#Search this address:
#https://www.google.com/maps/search/1600+Amphitheatre+Parkway,+Mountain+View,+CA+94043


address = input("Raw address: ").strip()

street, city, state_zip = address.split(", ")
state, zipcode = state_zip.split(" ")

print(f'''

Street: {street}
City: {city}
State: {state}
ZIP: {zipcode}

Search this address:
https://www.google.com/maps/search/{address.replace(' ', '+')}

''')
