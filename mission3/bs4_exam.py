from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
soup.prettify() # 들여쓰기된 html을 보여준다.

soup.title # 가장 먼저있는 title 테그를 가져온다.
# <title>The Dormouse's story</title>

soup.title.name # 타이틀 테그의 테그 이름을 가져온다.
# u'title

soup.title.string # 타이틀 테그안에 있는 글자
# u'The Dormouse's story'

soup.title.parent # 타이틀 테그의 부모 테그를 가져온다.
# <head><title>The Dormouse's story</title></head>
soup.title.parent.name # 타이틀 테그의 부모 테그의 이름을 가져온다.
# u'head'

soup.p # 가장 먼저 나오는 p 테그를 가져온다.
# <p class="title"><b>The Dormouse's story</b></p>
soup.p['class'] # 테그의 속성을 가져올때는 딕셔너리와 같은 문법을 사용하는듯 보인다.
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a') # 모든 a 테그를 가져온다.
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3") # find 함수에 id를 인자로 테그를 찾을 수 있다.
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

for link in soup.find_all('a'): # 페이지에 모든 링크를 찾을 때 유용해 보인다.
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

print(soup.get_text()) # 페이지의 모든 텍스트를 찾을 때 쓴다.
# The Dormouse's story
# . . .
# . . .