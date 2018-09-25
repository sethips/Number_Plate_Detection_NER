
import re 
def find_number_plate(text):
	email = re.findall(r'(([a-zA-Z]){2}\d{4})', text)
	return email
     
def get_task_1(text):
	number_plate = []

	dictionary = {}
	if find_number_plate(text):
		number_plate.extend(find_number_plate(text))

	dictionary["number_plate"] = number_plate

	return dictionary
