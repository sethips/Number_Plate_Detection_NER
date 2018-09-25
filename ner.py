

import polyglot
from polyglot.text import Text, Word
from polyglot.detect import Detector
import regular_expression_number_plate


def hardcoded_ner(text):
	dictionary = regular_expression_number_plate.get_task_1(text)
	return dictionary
def polyglot_ner(user_input):
	text = Text(user_input,hint_language_code='en')
	return [{entity.tag:entity} for entity in text.entities]

