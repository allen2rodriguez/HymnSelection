import wikipediaapi

# Initialize the Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(user_agent='MyProjectName')

# Get information about a page
page_py = wiki_wiki.page('Python_(programming_language)')
print(page_py.title)
print(page_py.summary)
print(page_py.links)

# Search for articles
results = wiki_wiki.search('machine learning')
for result in results:
    print(result.title)

# Get categories and members
cat = wiki_wiki.page('Category:Physics')
print(cat.categorymembers)