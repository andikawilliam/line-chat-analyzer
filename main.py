import yaml
from chat_cleaner import ChatCleaner
from text_manager import TextManager

def get_environment_settings():
    with open("env.yaml", 'r') as stream:
        try:
            # data = yaml.safe_load(stream)
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return data

data = get_environment_settings()
print(data)
file_folder = data['folder']
filename = data['filename']

ChatCleaner = ChatCleaner(filename, file_folder)

unwanted_strings = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
cleaned_file_location = ChatCleaner.clean_lines_starting_with_unwanted_strings(
        unwanted_strings
    )

TextManager = TextManager(cleaned_file_location)
TextManager.read_file_into_dataframe()

TextManager.delete_non_message_rows()
TextManager.rename_duplicate_author_identities(
    data['properties']['duplicate_authors']
)

TextManager.get_most_active_hours()

TextManager.get_authors_num_of_stickers()
TextManager.delete_sticker_and_photo_messages()

TextManager.get_authors_num_of_shares()
TextManager.get_authors_num_of_added_photo()
TextManager.delete_shares_and_add_photo_messages()

TextManager.reset_row_index_after_deletion()

TextManager.add_message_length_columns()

TextManager.get_authors_num_of_messages()
TextManager.get_authors_avg_of_message_length_str()
TextManager.get_authors_avg_of_message_length_words()

top_words = TextManager.count_unique_values(TextManager.df)
TextManager.generate_word_cloud(top_words)