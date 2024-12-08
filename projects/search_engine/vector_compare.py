import math  

class VectorCompare:
    """
    This class provides tools to calculate the similarity between two textual documents
    using vector space techniques.
    """

    def magnitude(self, concordance):
        """
        Calculate the magnitude (size) of a vector .

        Magnitude is computed as the square root of the sum of squared word counts.

        Args:
            concordance (dict): A dictionary with words as keys and their counts as values.

        Returns:
            float: The magnitude of the vector.

        Raises:
            ValueError: If the input is not a dictionary.
        """
        if type(concordance) != dict:
            raise ValueError('Supplied Argument should be of type dict')

        total = sum(count ** 2 for count in concordance.values())  # Sum of squares of word counts
        return math.sqrt(total)  # Square root of the sum

    def relation(self, concordance1, concordance2):
        """
        Calculate the cosine similarity between two vectors .

        Cosine similarity is calculated as:
        (Dot Product of Vectors) / (Magnitude of Vector1 * Magnitude of Vector2)

        Args:
            concordance1 (dict): Concordance of the first document.
            concordance2 (dict): Concordance of the second document.

        Returns:
            float: A number between 0 and 1 representing the similarity.

        Raises:
            ValueError: If the inputs are not dictionaries.
        """
        if type(concordance1) != dict:
            raise ValueError('Supplied Argument 1 should be of type dict')
        if type(concordance2) != dict:
            raise ValueError('Supplied Argument 2 should be of type dict')

        # Calculate the dot product of the two vectors
        dot_product = sum(
            concordance1[word] * concordance2.get(word, 0)  # Get the word count from concordance2 or 0 if missing
            for word in concordance1
        )

        # Calculate magnitudes of both vectors
        mag1 = self.magnitude(concordance1)
        mag2 = self.magnitude(concordance2)

        # Avoid division by zero by checking if either magnitude is zero
        if mag1 == 0 or mag2 == 0:
            return 0

        # Return cosine similarity
        return dot_product / (mag1 * mag2)

    def concordance(self, document):
        """
        Generate a concordance (word frequency count) for a given document.

        Args:
            document (str): The text document to process.

        Returns:
            dict: A dictionary with words as keys and their counts as values.

        Raises:
            ValueError: If the input is not a string.
        """
        if type(document) != str:
            raise ValueError('Supplied Argument should be of type string')

        con = {}
        for word in document.split():  # Split the document into words by spaces
            if word in con:
                con[word] += 1  # Increment the count if the word exists
            else:
                con[word] = 1  # Initialize the count for a new word
        return con


v = VectorCompare()

documents = {
  0:'''At Scale You Will Hit Every Performance Issue I used to think I knew a bit about performance scalability and how to keep things trucking when you hit large amounts of data Truth is I know diddly squat on the subject since the most I have ever done is read about how its done To understand how I came about realising this you need some background''',
  1:'''Richard Stallman to visit Australia Im not usually one to promote events and the like unless I feel there is a genuine benefit to be had by attending but this is one stands out Richard M Stallman the guru of Free Software is coming Down Under to hold a talk You can read about him here Open Source Celebrity to visit Australia''',
  2:'''MySQL Backups Done Easily One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases The first answer is usually use mysqldump This is all fine and good till you start to want to dump multiple databases You can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain''',
  3:'''Why You Shouldnt roll your own CAPTCHA At a TechEd I attended a few years ago I was watching a presentation about Security presented by Rocky Heckman read his blog its quite good In it he was talking about security algorithms The part that really stuck with me went like this''',
  4:'''The Great Benefit of Test Driven Development Nobody Talks About The feeling of productivity because you are writing lots of code Think about that for a moment Ask any developer who wants to develop why they became a developer One of the first things that comes up is I enjoy writing code This is one of the things that I personally enjoy doing Writing code any code especially when its solving my current problem makes me feel productive It makes me feel like Im getting somewhere Its empowering''',
  5:'''Setting up GIT to use a Subversion SVN style workflow Moving from Subversion SVN to GIT can be a little confusing at first I think the biggest thing I noticed was that GIT doesnt have a specific workflow you have to pick your own Personally I wanted to stick to my Subversion like work-flow with a central server which all my machines would pull and push too Since it took a while to set up I thought I would throw up a blog post on how to do it''',
  6:'''Why CAPTCHA Never Use Numbers 0 1 5 7 Interestingly this sort of question pops up a lot in my referring search term stats Why CAPTCHAs never use the numbers 0 1 5 7 Its a relativity simple question with a reasonably simple answer Its because each of the above numbers are easy to confuse with a letter See the below''',
}

index = {
0:v.concordance(documents[0].lower()),
1:v.concordance(documents[1].lower()),
2:v.concordance(documents[2].lower()),
3:v.concordance(documents[3].lower()),
4:v.concordance(documents[4].lower()),
5:v.concordance(documents[5].lower()),
6:v.concordance(documents[6].lower()),
}

searchterm = input('Enter Search Term: ')
matches = []

for i in range(len(index)):
  relation = v.relation(v.concordance(searchterm.lower()),index[i])
  if relation > 0:
    matches.append((relation,documents[i][:100]))

matches.sort(reverse=True)

for i in matches:
  print(i[0],i[1])