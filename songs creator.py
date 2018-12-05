# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 07:46:49 2018

@author: Sebastien
"""

import random

  
class Rank_UF:
    def __init__(self):
        self.words = set() # keeps words as a set
        self.parent = dict() # keeps the parent of each word in a dict
        self.rank = dict() # keeps rank of each word in a dict
        self.count = 0 # keeps track of number of disjoint unions
        
        
    def union(self, word1, word2):
        if self.is_connected(word1, word2): # if connected then they are connected
            return
        
        word1 = self.find_parent(word1) 
        word2 = self.find_parent(word2)
        
        if self.rank[word1] == self.rank[word2]: #if ranks equal then rank will change
            self.rank[word1] += 1
            self.parent[word2] = word1
        elif self.rank[word1]>self.rank[word2]: # if ranks different add node with smaller rank to big node
            self.parent[word2] = word1
        elif self.rank[word2]>self.rank[word1]:
            self.parent[word1] = word2
        self.count -= 1 # one less unconnected component
        
    def find_parent(self, word):
        if word == self.parent[word]: # if it is its own parent it returns itself
            return word
        self.parent[word] = self.find_parent(self.parent[word]) #else it reasigns its parent by the root parent of his parent
        return self.parent[word] # returns its root parent
    
    def insert(self, word):
        if word in self.words: # each word only once
            return
        
        self.words.add(word) # adds word to the UF
        self.parent[word] = word # it is its own parent to start with
        self.rank[word] = 0 # its rank is 0
        self.count += 1 # it creates a new seperated union
        
    def is_connected(self, word1, word2):
        return self.find_parent(word1) == self.find_parent(word2) # sees if they have the same parent
        
    def get_count(self):
        return self.count # number of seperated unions in the set of words
    
    def print_class(self, word = None):
        if word == None:
            word = random.sample(self.words,1)[0]
        return # i dont know what to do here this data structure isnt for this
    
    

class  Song:
    def __init__(self,name = 'song'):
        self.name = name
        self.size = 0
        self.words = [] # list of tuples with word and number of sylables
        self.rhyme = {}
        self.line_length = 20
        
    def add_word(self,word,syl,rhymes_with = []):
        self.words.append((word,syl))
        self.rhyme[word] = rhymes_with
        
    def define_song_structure(self):
        return

    def read_text_file(self,name = 'animals'):
        self.words = set()
        with open(name+'.txt','r') as file:
            for line in file.readlines():
                line = line.strip()
                if not line in  ['', 'Extinct', 'Critically Endangered', 'Endangered', 
                                 'Vulnerable', 'Threatened' , 'Near Threatened', 
                                 'Least Concern' , 'Common', 'Data Deficient', 'Not Listed' ]:
                    self.words.add(line)
        self.words = list(self.words)
        print(len(self.words))

    def pair_words(self):
        self.word_tree = Rank_UF()
        simple_rhymes_1 = ['o', 'a' ]
        for i,word1 in enumerate(self.words):
            for j,word2 in enumerate(self.words[i:]):
                self.word_tree.insert(word1)
                self.word_tree.insert(word2)
                if word1[-3:] == word2[-3:] or word1[-2:] == word2[-2:] or (word1[-1] == word2[-1] and word1[-1] in simple_rhymes_1):
                    self.word_tree.union(word1,word2)
                
    def save_pairs(self, name = 'paired_animals'):
        dict_write = dict()
        for word in self.words:
            p = self.word_tree.find_parent(word)
            if p in dict_write:
                dict_write[p].append(word)
            else:
                dict_write[p] = [word]
        with open(name+'.txt', 'w') as file:
            for parent in dict_write:
                file.write('---'.join(dict_write[parent]))
                file.write('\n \n')
                    
            
            
            
        
                    
        
        """
        
        bulldog, bullfrog, wild dog,  wharthog, Frog
        
        antelope
        
        gecko, flamingo, dingo, rhino, Buffalo, Flamingo, Armadillo, bongo, bonobo
        
        baracuda, cheetah, gorilla, Hyena, Impala, zebra , Akita
        
        donkey, coati, chimpanzee, booby, bumble bee,
        
        Gahrial, eagle, gerbil, coral, beagle, crocodile, whale, camel
        
        chipmunk, chinook, Fennec, shark, Aardvark, duck
        
        Giraffe
        
        Gnu 
        
        goose, discus, cuscus, Hippopotamus, Octopus, Albatross
        
        heron, falcon, dolphin, crane, chameleon, caiman, python, birman, Lion, sea lion, penguin, dolphin, bison
        
        baboon
        
        Leopard, bard, bird
        
        ferret, coyote, bat, Parrot, goat, elephant, wild cat, Suricate, avocet, bandicoot
        
        Ostrich, cockroach
        
        Fox
        
        Akbash, Angelfish,
        
        harrier, Hare, Hamster, gar, cougar, Anteater, Badger, bear, beaver, deer
        
        
        Axolotl, beetle
        
        butterfly
        
        cow
        
        crab
        
        havanese
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
