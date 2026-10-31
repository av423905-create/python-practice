letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
letter=letter.replace("<|Name|>","aman")
letter=letter.replace("<|Date|>","2023-10-10")
print(letter)