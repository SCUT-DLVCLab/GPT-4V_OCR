#encoding=utf-8
prefix = "You are a document understanding AI, who reads the contents in the given document image and tells the information that the user needs. Respond with the original content in the document image, do not reformat. No extra explanation is needed.\n"

prompt_1 = "Extract all the key-value pairs from the document image."
prompt_2 = "Extract all the key-value pairs from the document image. Response with a two-column markdown table."
prompt_3 = "Extract all the key-value pairs from the document image. Response in json formatted as [{\"key\": <key_content>, \"value\": <value_content>}, {\"key\": <key_content>, \"value\": <value_content>}, ...]"
