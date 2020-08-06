# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:32:48 2020

@author: jakem
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import scipy
import numpy as np

#Provided a corpus of documents in the form of a list, where each element is a single string of a document
#Produces relevant TF-IDF values for all unique words for each document
class key_word_document_retriever(): 
    '''
    @params:
    corpus: list data type 
    
    purpose:
    do some TFIDF and n-gram methods to extract key_words
    ''' 
    
    def __init__(self, corpus):
        
        # initilise variable
        self.c = corpus
        self.tfidf_mat, self.vocab = self.get_tfidf() #Get TF-IDF weightings for corpus
        
    def get_tfidf(self):
        '''
        Performs TF-IDF onto corpus of documents.
        @returns:
            tfidf_mat: matrix of TF-IDF weightings where entry (i,j) represents the TF-IDF weighting of word j in document i
            vocab: array of unique words in the entire corpus
        '''
        # get model call it vectoriser
        vectorizer = TfidfVectorizer()
        # transform corpus via model and store result of tfidf weightings for each document into variable named X, 
        #where entry i,j is the tfidf weighting of word j in document i
        tfidf_mat = scipy.sparse.csr_matrix.toarray(vectorizer.fit_transform(self.c))
        # get the feature names for each document, store those words to variable vocabulary
        vocab = np.array(vectorizer.get_feature_names())
        return tfidf_mat, vocab
    
    def get_words(self, doc_idx, num_key_words=3):
        '''
        Provided a documents index in the original corpus, returns a specified number of key words with the largest TF-IDF weightings
        @params:
            doc_idx: index of the document in the corpus
            num_key_words: top n key words to be returned
        '''
        key_words_idx = np.array(self.tfidf_mat.argsort()[doc_idx][-num_key_words:][::-1])
        key_words = np.array(self.vocab)[key_words_idx]
        return key_words
    
    def get_word_idx(self, word):
        '''
        Provided a word, returns its position in the vocabulary vector
        '''
        if(len(np.where(self.vocab == word)[0]) != 0):
            word_idx = np.where(self.vocab == word)[0][0] #Index of word in vocabulary
            return word_idx
        else:
             print("'{}' does not exist in the corpus".format(word))

    
    def get_docs(self, word, num_documents=3):
        '''
        Provided a word, returns a specified number of documents where the word in question has the most importance
        @params:
            word: term to use to find the documents such that the word has the most relevance
            num_documents: number of documents in the corpus to return
            
        @returns:
            relevant_documents: Full text of documents returned such that the specified word has the most relevance to
            relevant_documents_idx: Index in corpus of relevant documents
        '''
        if len(word.split()) == 1:
            word_idx = self.get_word_idx(word)
            ordered_doc_idx = self.tfidf_mat[:,word_idx].argsort() #Ordered documents in ascending order, ordered by 'relevance' of the specified word
            relevant_documents_idx = ordered_doc_idx[-num_documents:][::-1] 
            relevant_documents = self.c[relevant_documents_idx] #Documents where the specified word has the most relevance
            return relevant_documents, relevant_documents_idx
        
        else:
            terms = word.split()
            relevant_terms_tfidf = []
            for term in terms:
                word_idx = self.get_word_idx(term)
                relevant_tfidf = self.tfidf_mat[:, word_idx]
                relevant_terms_tfidf.append(relevant_tfidf)
            relevant_terms_tfidf = np.log(np.array(relevant_terms_tfidf))
            combined_tfidf = sum(relevant_terms_tfidf)
            ordered_doc_idx = combined_tfidf.argsort()
            relevant_documents_idx = ordered_doc_idx[-num_documents:][::-1] 
            relevant_documents = self.c[relevant_documents_idx] #Documents where the specified word has the most relevance
            return relevant_documents, relevant_documents_idx