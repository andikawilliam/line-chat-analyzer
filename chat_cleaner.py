import re
class ChatCleaner():

	def __init__(self, filename, file_folder):
		self.filename = filename
		self.file_folder = file_folder
		self.file_location = "chat_history/{folder}/original/{filename}".format(
			folder=self.file_folder, filename=self.filename
		)

	def clean_lines_starting_with_unwanted_strings(self, unwanted_strings):
		cleaned_filename = ('cleaned_%s' % self.filename)
		cleaned_file_location = "chat_history/{folder}/cleaned/{filename}".format(
			folder=self.file_folder, filename=cleaned_filename
		)

		with open(self.file_location) as textfile, open(cleaned_file_location, 'w') as cleaned_file:
			for line in textfile:
				if self.string_fits_criteria(line, unwanted_strings):
					cleaned_file.write(line)
		return cleaned_file_location
				
	def string_fits_criteria(self, line, unwanted_strings):
		if not line.isspace():
			if not line.startswith(unwanted_strings):
				if self.check_if_string_is_time(line):
					return True

	def check_if_string_is_time(self, strings):
		match = re.match(r'(^\d\d:\d\d\t)', strings[:6])
		if match:
			return True
		else:
			return False
