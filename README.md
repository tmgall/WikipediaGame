# Wikipedia Game Algorithm

The Wikipedia Game is an online challenge where the player starts at a random Wikipedia page and attempts to get to another page (chosen at random or by the player) by only clicking hyperlinks from within the Wikipedia article. Additional rules sometimes include forbidding list articles or countries, doing this in the fewest number of clicks, etc, but this code only uses the basic ruleset (i.e. the pathing may go through a country or a list). 

This code implements a Breadth First Search beginning at the start article, so it will find one of the shortest paths to the destination. There is often more than one way to get from the start article to the destination article in the fewest number of clicks, so this algorithm just returns the first one it comes across, but it is guaranteed that there is no faster path. 

PLEASE NOTE: This algorithm is incredibly slow. The logic is optimized, but the webpage requests in order to find which links are on a given page takes up the bulk of the time. The sample run that I use in the code took about a half an hour on Google Colab. This could be improved if there exists some sort of open source database that would eliminate this lengthy request time.

To change the start and destination articles, simply copy and paste the URLs of each article on Wikipedia into the start and destination strings at the bottom and it should run!
