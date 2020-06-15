import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

import pprint

# TO DO : 
# VIsualize each table using barchart
# - Each author is assigned a unique color
# - Explore a professional looking barchart, how to draw a visually
# - Instead of creating a new dataframe, also add it to the main dataframe file

# AHEAD:
# See how to connect website to python code

class TextManager():

	def __init__(self, file_location):
		self.file_location = file_location
		self.LONG_LINE = "="*90

	def read_file_into_dataframe(self):
		self.df = pd.read_csv(self.file_location, names=['time'])
		self.df[['time', 'author', 'message']] = self.df['time'].str.split('\t', 2, expand=True)
		
	def delete_non_message_rows(self):
		author_actions = ["joined", "invited", "removed", "left", "changed", "canceled","disabled"]
		self.df = self.df[~self.df['author'].str.contains('|'.join(author_actions))]
		self.df = self.df[self.df['message'].notna()]

	def rename_duplicate_author_identities(self, duplicate_identities):
		duplicates = duplicate_identities
		for pseudonym, real_author in duplicates.items():
			self.df['author'] = self.df['author'].str.replace(pseudonym, real_author, regex=True)

	def get_most_active_hours(self):
		self.df_active_hours = self.df
		self.df_active_hours['time'] = self.df_active_hours['time'].astype(str).str[:2]
		self.df_active_hours = self.df_active_hours.groupby(
			'time').size().reset_index(
			name='message_count'
		)
		print(self.df_active_hours)
		print(self.LONG_LINE)

	def get_authors_num_of_stickers(self):
		self.sticker_photo = ["[Sticker]", "[Photo]"]

		self.df_sticker_count = self.df[self.df['message'].isin([self.sticker_photo[1]])].groupby(
			'author').size().sort_values().reset_index(name='sticker_message_count')
		print(self.df_sticker_count)
		print(self.LONG_LINE)

	def delete_sticker_and_photo_messages(self):
		self.df = self.df[~self.df['message'].isin(self.sticker_photo)]

	def get_authors_num_of_shares(self):
		self.df_shares_count = self.df[self.df['message'].str.contains("shared")].groupby(
			'author').size().sort_values().reset_index(name='share_count')
		print(self.df_shares_count)
		print(self.LONG_LINE)

	def get_authors_num_of_added_photo(self):
		self.df_add_photo_count = self.df[self.df['message'].str.contains("added")].groupby(
			'author').size().sort_values().reset_index(name='add_photo_count')
		print(self.df_add_photo_count)
		print(self.LONG_LINE)

	def delete_shares_and_add_photo_messages(self):
		message_keywords = ["added", "shared", "created"]
		self.df = self.df[~self.df['message'].str.contains('|'.join(message_keywords))]
		# self.df = self.df[~self.df['author'].str.contains('|'.join(author_actions))]

	def add_message_length_columns(self):
		self.df['message_length_str'] = self.df['message'].str.len()
		self.df['message_length_words'] = self.df['message'].str.split().str.len()
		
	def reset_row_index_after_deletion(self):
		self.df = self.df.reset_index(drop=True)
	
	def get_authors_num_of_messages(self):
		self.df_message_count = self.df.groupby(
			'author').size().sort_values().reset_index(
			name='message_count'
		)
		print(self.df_message_count)
		print(self.LONG_LINE)

	def get_authors_avg_of_message_length_str(self):
		self.df_message_str_length = self.df.groupby(
			'author')['message_length_str'].mean().sort_values().reset_index(
			name='message_length_str'
		)
		print(self.df_message_str_length)
		print(self.LONG_LINE)

	def get_authors_avg_of_message_length_words(self):
		self.df_message_word_length = self.df.groupby(
			'author')['message_length_words'].mean().sort_values().reset_index(
			name='message_length_words'
		)
		print(self.df_message_word_length)
		print(self.LONG_LINE)

	def lowercase_and_split_messages(self):
		self.df['message'].str.lower().str.split()

	def count_unique_values(self, dataframe):
		results = Counter()
		dataframe['message'].str.lower().str.split().apply(results.update)

		pp = pprint.PrettyPrinter(indent=4)
		top_words = results.most_common(50)
		print("TOP WORDS")
		pp.pprint(top_words)
		return top_words
		
	def generate_word_cloud(self, top_words):
		wordcloud = WordCloud()
		wordcloud.generate_from_frequencies(dict(top_words))
		plt.imshow(wordcloud)
		plt.axis("off")
		plt.show(block=False)
		plt.pause(10)
		plt.close()
		