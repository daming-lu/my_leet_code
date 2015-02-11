# author
# +----+-----------------------+
# | id | name                  |
# +----+-----------------------+
# | 1  | Neil Gaiman           |
# | 2  | Sir Arthur Conan Doyle|
# | 3  | Terry Pratchett       |
# | 4  | Snooki                |
# +----+-----------------------+
#
# book
# +---+------------------------------------+
# | id | title                             |
# +----+-----------------------------------+
# | 1  | Good Omens                        |
# | 2  | The Adventures of Sherlock Holmes |
# | 3  | Stardust                          |
# | 4  | Epic of Gilgamesh                 |
# +----+-----------------------------------+
#
# author_book
# +-----------+---------+
# | author_id | book_id |
# +-----------+---------+
# | 1         | 1       |
# | 1         | 3       |
# | 2         | 2       |
# | 3         | 1       |
# +-----------+---------+
#
# Return the names of all authors who have written at least one book
#
#
# SELECT a.name FROM author a, book b, author_book ab
# WHERE
# a.id == ab.author_id
# AND
# b.id == ab.book_id
# AND
#


__author__ = 'daming'
def doX(string):
    array = string.split("\n")
    output = []
    for line in array:
        output.append(helper(line))
    output = helper2(output)
    return "\n".join(output)

def helper2(array):
    retArray = []
    for item in array:
        if (item != None and item != ""):
            retArray.append(item)
    return retArray

def helper(line):
    regex = re.compile("(\(\d{3}\)\s*|\d{3}-)\d{3}-\d{4}")
    lineArray = line.split(' ')
    if len(lineArray)<2:
        return ""
    try:
        value = lineArray[1]
    except IndexError:
        return ""
    match = regex.match(value)
    if match:
        return match.group()
    else:
        return ""

print doX("Zach 919-645-2009\n" +
        "John 212-454-2000\n" +
        "Alex 2A2-342-4000\n" +
        "Fred 22-453-2334\n" +
        "Camille 343-3432-453\n" +
        "Sarah 454-654-8700\n" +
        "Eric345-434-2334\n" +
        "Francis 453-ask-fran")
