import difflib

text1 = '''Hello, How are You
Can u find the difference?
'''

text2 = '''Hellow, how are you
Can u find the differencce?
'''

delta = difflib.Differ().compare(text1.splitlines(), text2.splitlines())
print("\n".join(delta))
