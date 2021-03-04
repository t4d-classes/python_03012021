import re

# r = re.compile(r'bee')
# content = "as busy as a bee"

# r = re.compile(r'<span>.*</span>')
# r = re.compile(r'<.*?>(.*?)</.*?>')
# content = "<b>content 1</b><span>test</span><b>content 2</b><div>fun</div>"


# first match and it must match from the start of the file
# print(r.match(content))

# use search to find all match by processing the content until the end
# match = r.search(content)
# while match:
#     print(match)
#     start, end = match.span()
#     match = r.search(content, end)

# text matches, location in content does not matter
# for match in r.findall(content):
#     print(match)

# search all the content and return match objects for all matches
# for match in r.finditer(content):
#     print(match.group(0))

# content = "red|green;blue:orange"
# r = re.compile("\||;|:")
# r = re.compile("[|;:]")
# print(r.split(content))
# print(r.sub(",", content))

content = """apple
banana
apple
banana
banana
Apple
"""

r = re.compile(r"^a[a-z]*", re.MULTILINE | re.IGNORECASE)
# r = re.compile(r"[a-z]*a$", re.MULTILINE)
for match in r.finditer(content):
    print(match)

