import phonenumbers

from phonenumbers import geocoder, carrier, timezone

print("//"*15)

number=input("Enter The Phone Number: ")

phone_num=phonenumbers.parse(number,None)
print("-------------------------------------------------------")
print("The Country Code is: ",phone_num.country_code)

print("-------------------------------------------------------")

print("The National Number is: ", phone_num.national_number)

print("-------------------------------------------------------")

print("The country of this Number is: ", geocoder.description_for_number(phone_num,'en'))

print("-------------------------------------------------------")

print("The Companey for this Number is: : ", carrier.name_for_number(phone_num,'en'))

print("-------------------------------------------------------")

print("The Time Zone For this Number is: ",timezone.time_zones_for_geographical_number(phone_num))

print("-------------------------------------------------------")
