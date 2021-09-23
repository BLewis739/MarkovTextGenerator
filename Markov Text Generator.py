# Markov Text Generator.py
# Adapted from problem set question in Boston University course CS111
# Professor David Sullivan, PhD
# This version written by Brad Lewis 9/22/21

import random

'''
create_dictionary takes in a string that refers to the name
of a text file in the folder of the program. It returns d,
which is a dictionary containing the text of the program.
'''
def create_dictionary(filename):

    nfile = open(filename, 'r', encoding='utf8')
                                   
    d = {'$': []}                                   #Create dictionary with $ as key to refer to sentence starters

    for line in nfile:
       
        line = line[:-1]                            #eliminate the \n character
        words = line.split(" ")                     #create a list by removing the spaces

        if line != '':                              #only adds words for non-null lines
            d['$'].append(words[0])                 #First word of line assigned to $ key
            for i in range(len(words)):             #scan word-by-word to add
                
                
                if i + 1 != len(words) and words[i+1] != '':    #Only adds words if there is a word after AND the word after isn't null

                    if words[i] == '':              #Assigns starts of sentences after nulls to $
                        d['$'].append(words[i+1])

                    elif words[i] in d:             #Assigns words already in d a new key
                        d[words[i]].append(words[i+1])
      
                    else:                           #Makes new keys 
                        d[words[i]] = [words[i+1]]    
    nfile.close()                                   #close the file
    return d
    
def generate_text(d,num_words):                     #d is the dictionary inputted, num_words is desired length of the output
    
    count = 0
    text = ''
    pun_list = ['.', '?', '!', ':']
    abbrev_list = ['Mr.', 'Ms.', 'Mrs.', 'Dr.', 'etc.', 'vs.', 'Vs.']
    
    while count < num_words:                        #Continues adding text as long as output hasn't yet hit the desired length
        
        sent = []                                   #sentence
        first_word = ''                             
        while first_word == '':
            first_word = random.choice(d['$'])      #Pick the first word
        sent.append(first_word)                     #First word is added to the empty sentence

        if first_word in d:
            
            if len(d[first_word]) > 1:              #Applied to keys that have multiple possible values
                next_word = random.choice(d[first_word])
            else:
                one_word_list = d[first_word]       #For keys that have only one possible option
                next_word = one_word_list[0]
            
            sent.append(next_word)                  #next_word is determined above, appended to sentence here

            while next_word in d:                   #Continues adding words as long as next_word is a key in d

                if len(d[next_word]) > 1:           #Randomly chooses value if key has multiple values
                    next_word = random.choice(d[next_word])

                else:                               #If key has only one value, it is automatically picked
                    one_word_list = d[next_word]
                    next_word = one_word_list[0]

                sent.append(next_word)    
                                                    #Check for punctuation
                if next_word not in abbrev_list:    #Ignore punctuation on common abbreviations
                    if next_word[-1] in pun_list:   #Identify punction that ends sentences
                        break

            for i in sent:                          #Convert list of text into a string
                text = text + i + " "
            count += len(sent)                      #Update count based on the number of words added
            text += '\n'                            #Add a newline character to the end for better readability
    print(text)

d = create_dictionary("/Users/terrordome/Desktop/Projects/Markov Text Generator/NepWxT.txt")
generate_text(d, 150)
    
    
    



    
