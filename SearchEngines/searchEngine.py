import crawler

def init_crawler():
	global index, graph
	index, graph = crawl_web('https://en.wikipedia.org/wiki/India')

graph = {}  # <url>, [list of pages it links to]
index = {}