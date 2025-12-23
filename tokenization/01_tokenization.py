import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

text = "Hi, How are you?"

encoder_text = encoder.encode(text)

print(f"Input text: {text}")

print("=="*30)

print(f"Encoder output: {encoder_text}")

decoded_text = encoder.decode(encoder_text)

print(f"Decoder output: {decoded_text}")