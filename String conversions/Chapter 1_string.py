text = "X-DSPAM-Confidence:    0.8475"
first_number_in_text = text.find(" ")
last_number_in_text = text.find("5")
final_number = text[first_number_in_text: last_number_in_text+1]
print(float(final_number))






