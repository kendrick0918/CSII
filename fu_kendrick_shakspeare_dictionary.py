import string

'''
fu_Kendrick_shakespeare_dictionary.py

Description: This script reads a shakespeare text file, 
cleans the text by removing punctuation and converting to lowercase, 
filters out common "stop words," and counts the frequency of the remaining 
meaningful(words that tell a story) words. The top 30 most frequent words are then saved to a CSV file.

list of completed functions: shakespeare, writecsv
'''

stop_words = ['tell','and', 'or', 'i', 'the', 'a', 'to', 'of', 'in', 'is', 'it', 'that', 'you', 'my', 'not','with','his','be','have','but','your','he','our','me','for','what','all','so','as','him','we','do','are','will','which','no','on','this','they','from','yet','by','if','now','her','shall','o','thy','thee','she','then','here','an','go','am','thou','when','come','when','us','there','upon','at','them','and','hath','would','was','time','well','who','should','did','like','were','make','where','done','let','how','had','may','see','speak','one','must','why','most','say','tis','ill','their','more','man','no','sir','than','out','second','out','mine','too','up','before','can','nor','does','such','those','give','look','enter','some','never','these','know','thorugh','true','take','away','wood','doth','thus','third','much','good','ay','word','back']
counts = dict() 
def shakespeare():
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

        #these next few lines just sort the words into analyzable data
    
    for line in fhand: 
        line = line.rstrip()
        # First two parameters are empty strings
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words: 
            if word not in stop_words: #filters words thorugh the stopword list
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
    print(counts)

    
def writecsv():
    try:
        with open("write.csv", 'w') as outfile: 

            outfile.write("words,Count\n") 

            sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True) #counts the top 20 most frequent words from the list of words we already have created
            top_20 = sorted_items[:20] #got this code off of internet
            

            for key, value in top_20:
                row = f"{key},{value}\n" #formats the data that your pulling in the CSV as (words,count)
                outfile.write(row)
    
        print("yes") #testing to see if code reaches this point
    except Exception as e:
        print("an error occured:", e)


def main():
    shakespeare()
    writecsv()
main()