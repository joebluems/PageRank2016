# PageRank2016
Using the PageRank algorithm to analyze the teams playing in the NCAA Basketball Tournament

### Resources
Google's PageRank and Beyond - Langville, Meyer<BR>
http://www.amazon.com/gp/product/0691152667?keywords=google's%20page%20rank&qid=1458482177&ref_=sr_1_5&sr=8-5
<BR>
Downloading GNU Octave - https://www.gnu.org/software/octave/download.html<BR>

### Running the program
1. ./grab.py - pulls scores from reference site for date range and stores as html 
2. ./read.py - reads raw HTML scores and writes out one record per game (teams and scores)
3. python map.py > H.mat - creates H matrix and "teams" file
4. octave page.m - produces page ranks
