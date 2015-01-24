from bs4 import BeautifulSoup

people = []
f = open('test_vote.html', 'r')
soup = BeautifulSoup(f.read())
for vote_part in soup.find(class_="statistics").find_all("td"):
	if vote_part.toString() != "<td class=\"noBorder\"> </td>":
		print vote_part

