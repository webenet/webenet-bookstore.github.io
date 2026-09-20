import json,re, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
# Title | author | reference USD; these reference amounts are NOT asserted as independently verified prices.
sections = {
'Horror': '''The Shining|Stephen King|20.00
It|Stephen King|22.00
Pet Sematary|Stephen King|19.99
Carrie|Stephen King|18.00
The Haunting of Hill House|Shirley Jackson|17.00
Dracula|Bram Stoker|12.00
Frankenstein|Mary Shelley|11.00
Mexican Gothic|Silvia Moreno-Garcia|18.00
The Only Good Indians|Stephen Graham Jones|18.99
The Exorcist|William Peter Blatty|18.00
Home Before Dark|Riley Sager|15.60
The Hollow Places|T. Kingfisher|13.61''',
'Action & Adventure': '''The Da Vinci Code|Dan Brown|18.99
Angels & Demons|Dan Brown|18.99
Inferno|Dan Brown|19.00
The Lost Symbol|Dan Brown|19.00
Jurassic Park|Michael Crichton|18.00
The Lost World|Michael Crichton|18.99
Treasure Island|Robert Louis Stevenson|9.99
The Count of Monte Cristo|Alexandre Dumas|16.00
The Three Musketeers|Alexandre Dumas|15.00
The Bourne Identity|Robert Ludlum|19.00
The Hunt for Red October|Tom Clancy|19.00
The Maze Runner|James Dashner|12.99''',
'Romance': '''It Ends with Us|Colleen Hoover|17.99
It Starts with Us|Colleen Hoover|17.99
Ugly Love|Colleen Hoover|16.99
Reminders of Him|Colleen Hoover|17.99
Book Lovers|Emily Henry|17.00
Beach Read|Emily Henry|17.00
People We Meet on Vacation|Emily Henry|17.00
Happy Place|Emily Henry|19.00
The Love Hypothesis|Ali Hazelwood|17.00
Love on the Brain|Ali Hazelwood|17.00
The Hating Game|Sally Thorne|17.00
The Notebook|Nicholas Sparks|17.99''',
'Mystery & Thriller': '''The Silent Patient|Alex Michaelides|12.99
Gone Girl|Gillian Flynn|18.00
The Girl on the Train|Paula Hawkins|18.00
The Housemaid|Freida McFadden|17.99
The Housemaid's Secret|Freida McFadden|17.99
Verity|Colleen Hoover|17.99
The Guest List|Lucy Foley|18.99
The Paris Apartment|Lucy Foley|18.99
The Woman in the Window|A. J. Finn|18.00
Big Little Lies|Liane Moriarty|18.00
The Thursday Murder Club|Richard Osman|18.00
And Then There Were None|Agatha Christie|15.99''',
'Fantasy': '''A Court of Thorns and Roses|Sarah J. Maas|14.24
A Court of Mist and Fury|Sarah J. Maas|19.00
Fourth Wing|Rebecca Yarros|20.00
Iron Flame|Rebecca Yarros|22.00
The Hobbit|J. R. R. Tolkien|17.00
The Fellowship of the Ring|J. R. R. Tolkien|18.99
The Two Towers|J. R. R. Tolkien|18.99
The Return of the King|J. R. R. Tolkien|18.99
The Name of the Wind|Patrick Rothfuss|18.00
Mistborn|Brandon Sanderson|19.99
Six of Crows|Leigh Bardugo|18.99
Graceling|Kristin Cashore|16.99''',
'Science Fiction': '''Project Hail Mary|Andy Weir|22.00
The Martian|Andy Weir|18.00
Dune|Frank Herbert|18.99
Dune Messiah|Frank Herbert|18.00
Ready Player One|Ernest Cline|18.00
Ender's Game|Orson Scott Card|19.00
The Three-Body Problem|Cixin Liu|18.99
Dark Matter|Blake Crouch|18.00
Recursion|Blake Crouch|18.00
Station Eleven|Emily St. John Mandel|18.00
Red Rising|Pierce Brown|18.00
Dungeon Crawler Carl|Matt Dinniman|20.00''',
'Literary Classics': '''Pride and Prejudice|Jane Austen|10.00
Jane Eyre|Charlotte Brontë|12.00
Wuthering Heights|Emily Brontë|11.00
1984|George Orwell|16.00
Animal Farm|George Orwell|12.00
To Kill a Mockingbird|Harper Lee|18.00
The Great Gatsby|F. Scott Fitzgerald|12.00
Little Women|Louisa May Alcott|12.00
The Picture of Dorian Gray|Oscar Wilde|11.00
The Catcher in the Rye|J. D. Salinger|17.00
The Alchemist|Paulo Coelho|17.99
One Hundred Years of Solitude|Gabriel García Márquez|18.00''',
'Young Adult': '''The Hunger Games|Suzanne Collins|14.99
Catching Fire|Suzanne Collins|14.99
Mockingjay|Suzanne Collins|14.99
The Fault in Our Stars|John Green|13.99
Looking for Alaska|John Green|14.99
The Perks of Being a Wallflower|Stephen Chbosky|16.99
Eleanor & Park|Rainbow Rowell|16.99
They Both Die at the End|Adam Silvera|16.99
One of Us Is Lying|Karen M. McManus|13.99
The Hate U Give|Angie Thomas|15.99
The Book Thief|Markus Zusak|14.99
We Were Liars|E. Lockhart|13.99''',
'Personal Growth': '''Atomic Habits|James Clear|27.00
The 7 Habits of Highly Effective People|Stephen R. Covey|19.99
The Power of Habit|Charles Duhigg|18.99
The Subtle Art of Not Giving a F*ck|Mark Manson|18.99
The Four Agreements|Don Miguel Ruiz|12.95
Think and Grow Rich|Napoleon Hill|12.99
The Mountain Is You|Brianna Wiest|19.99
The Courage to Be Disliked|Ichiro Kishimi|18.00
Deep Work|Cal Newport|20.00
The Psychology of Money|Morgan Housel|19.99
Can't Hurt Me|David Goggins|22.00
The Let Them Theory|Mel Robbins|29.99''',
'Business & Finance': '''Rich Dad Poor Dad|Robert T. Kiyosaki|19.95
The Lean Startup|Eric Ries|18.00
Zero to One|Peter Thiel|18.00
Good to Great|Jim Collins|32.00
Start with Why|Simon Sinek|19.00
The Intelligent Investor|Benjamin Graham|24.99
The $100 Startup|Chris Guillebeau|18.00
Shoe Dog|Phil Knight|20.00
The Personal MBA|Josh Kaufman|23.00
Never Split the Difference|Chris Voss|19.99
The Millionaire Next Door|Thomas J. Stanley|19.00
The E-Myth Revisited|Michael E. Gerber|22.00''',
'History & Biography': '''Sapiens|Yuval Noah Harari|24.99
Homo Deus|Yuval Noah Harari|22.99
Educated|Tara Westover|18.99
Becoming|Michelle Obama|20.00
Steve Jobs|Walter Isaacson|22.00
Leonardo da Vinci|Walter Isaacson|22.00
The Diary of a Young Girl|Anne Frank|12.99
The Wright Brothers|David McCullough|18.99
Unbroken|Laura Hillenbrand|20.00
Born a Crime|Trevor Noah|19.00
The Immortal Life of Henrietta Lacks|Rebecca Skloot|18.00
The Splendid and the Vile|Erik Larson|20.00''',
'Kids & Family': '''The Very Hungry Caterpillar|Eric Carle|10.99
Where the Wild Things Are|Maurice Sendak|19.99
Goodnight Moon|Margaret Wise Brown|9.99
The Cat in the Hat|Dr. Seuss|9.99
Green Eggs and Ham|Dr. Seuss|9.99
The Gruffalo|Julia Donaldson|10.99
Matilda|Roald Dahl|10.99
Charlie and the Chocolate Factory|Roald Dahl|9.99
Harry Potter and the Sorcerer's Stone|J. K. Rowling|12.99
Harry Potter and the Chamber of Secrets|J. K. Rowling|12.99
Wonder|R. J. Palacio|12.99
Diary of a Wimpy Kid|Jeff Kinney|14.99'''
}
verified={
('The Shining','Stephen King'):(20.00,'https://www.penguinrandomhouse.com/books/92991/the-shining-by-stephen-king/','Publisher list price, paperback'),
('It','Stephen King'):(22.00,'https://www.barnesandnoble.com/w/it-stephen-king/1100623119?ean=9781501182099','Retailer listed paperback'),
('Home Before Dark','Riley Sager'):(15.60,'https://www.target.com/p/home-before-dark-by-riley-sager-paperback/-/A-82073943','Retailer listed paperback'),
('The Hollow Places','T. Kingfisher'):(13.61,'https://www.target.com/p/the-hollow-places-by-t-kingfisher-paperback/-/A-92322853','Retailer listed paperback'),
('The Silent Patient','Alex Michaelides'):(12.99,'https://shop.barnesandnoble.com/products/9781250301710','Retailer listed edition'),
('A Court of Thorns and Roses','Sarah J. Maas'):(14.24,'https://www.walmart.com/c/best-sellers/books-fantasy-romance','Retailer listed paperback'),
('Graceling','Kristin Cashore'):(16.99,'https://shop.barnesandnoble.com/products/9780547258300','Retailer listed edition'),
('Project Hail Mary','Andy Weir'):(22.00,'https://www.bookweb.org/news/indie-scififantasy-bestseller-list-1632923','Bookseller list price'),
('Red Rising','Pierce Brown'):(18.00,'https://www.bookweb.org/news/indie-scififantasy-bestseller-list-1632923','Bookseller list price'),
('Dungeon Crawler Carl','Matt Dinniman'):(20.00,'https://www.bookweb.org/news/indie-scififantasy-bestseller-list-1632923','Bookseller list price'),
}
isbns={
('The Shining','Stephen King'):'9780345806789',('It','Stephen King'):'9781501182099',
('Home Before Dark','Riley Sager'):'9781524745196',('The Silent Patient','Alex Michaelides'):'9781250301710',
('Graceling','Kristin Cashore'):'9780547258300',('Red Rising','Pierce Brown'):'9780345539809',
('Dungeon Crawler Carl','Matt Dinniman'):'9780593820254',
}
books=[]
for i,(category, entries) in enumerate(sections.items()):
 for j,line in enumerate(entries.splitlines()):
  title,author,price=line.split('|')
  record={'id':f'wb-{i+1:02d}-{j+1:02d}','title':title,'author':author,'category':category,'price':float(price),'priceStatus':'reference','format':'Edition varies','isbn':isbns.get((title,author),''),'sourceUrl':'','sourceNote':'','badge':('Reader favorite' if j==0 else 'Discover' if j==1 else '')}
  if (title,author) in verified:
   p,url,note=verified[(title,author)]; record.update(price=p,priceStatus='sourced',sourceUrl=url,sourceNote=note,format='See linked edition')
  books.append(record)
assert len(books)==144 and len({(b['title'],b['author']) for b in books})==144
(ROOT/'data'/'books.json').write_text(json.dumps(books,ensure_ascii=False,indent=2),encoding='utf-8')
# js literal works with file:// without fetch
(ROOT/'js'/'catalog.js').write_text('window.WEBENET_BOOKS = '+json.dumps(books,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print('Books:',len(books),'Categories:',len(sections),'Verified prices:',len(verified))
