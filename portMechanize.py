import mechanize

def viewCode(url):
	browser = mechanize.Browser()
	page = browser.open(url)
	source_code = page.read()
	print(source_code)

viewCode("https://www.shodan.io/search?query=android+debug+bridge+country%3A%22US%22")