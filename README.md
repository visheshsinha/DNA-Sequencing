_Note : All the Rendered Juypter Notebooks(in nbviewer) for better view are availabe by clicking on the links embedded below. Also some links might not work so you can direcly [click here](https://nbviewer.jupyter.org/) and paste the link of the notebook you want to render_


### [DNA Sequencing](https://nbviewer.jupyter.org/github/visheshsinha/DNA_Sequencing/blob/master/DNA_Sequencing.ipynb?flush_cache=flase) 

DNA Sequencing is the process of determining the nucleic acid sequence – the order of nucleotides in DNA. It includes any method or technology that is used to determine the order of the four bases: _Adenine(A)_, _Guanine(G)_, _Cytosine(C)_, and _Thymine(T)_.
DNA Sequencing may be used to determine the sequence of individual genes, larger genetic regions (i.e. clusters of genes or operons), full chromosomes, or entire genomes of any organism. DNA sequencing is also the most efficient way to indirectly sequence RNA or proteins.

![N|Solid](https://www.jax.org/-/media/jaxweb/images/news-and-insights/blog/bridging-the-gaps.jpg?la=en&hash=4581A21A2B4E7FD89D8DA9501EA65C6B3EA8F28E)

#### Read Alignment Algorithms Covered : 
- #### Online Algorithms: 
    The algorithm in which the text 'T' (in our case the reference genome) is not pre-processed, and it doesn't matter if the pattern 'P' is pre-processed or not.
    - ##### [Naive Exact Matching Algorithm](https://github.com/visheshsinha/DNA_Sequencing/blob/master/naive_algo.py) : 
         >We niether pre-process 'P' nor 'T'.
    - ##### [Boyer-Moore (using Z-Algorithm)](https://nbviewer.jupyter.org/github/visheshsinha/DNA_Sequencing/blob/master/Boyer's_Moore_Pattern_Matching.ipynb?flush_cache=true) :
         >Here we pre-process 'P' but not 'T' so it's online.
        
        - ##### Text Resource : Go Through Chapter 2 of [Algorithms on Strings, Trees, and Sequences( by Dan Gusfield)](https://doi.org/10.1017/CBO9780511574931)
        - ##### Video Resource : Linear-time pattern matching : Z-values and Z-algorithm ( by Dan Gusfield) [Part 1](https://youtu.be/MFK0WYeVEag) [Part 2](https://youtu.be/NVJ_ELSbbew)

- #### Offline Algorithms: 
    The algorithm in which the text 'T' is  pre-processed, and it doesn't matter if the pattern 'P' is pre-processed or not.

    - ##### [SubString Indexing, k-mer index](https://nbviewer.jupyter.org/github/visheshsinha/DNA_Sequencing/blob/master/Indexing_K-mer.ipynb?flush_cache=flase) : 
    
    > We use the term k-mer to refer to a substring of length k. For each offset that the index reports back, that's called an index hit. When P matches within T, we've been calling that a match, or an occurrence. But, an index hit may or may not correspond to a match, it's just a hint that we should look harder in that particular region of T. So, not all index hits lead to matches, because we don't know whether the rest of P matches where it should within T. We have to do more character comparisons. And, this additional work that we do is called verification.
    >
    > This kind of data structure is called a multimap. It's a map because it associates keys, k-mers, in this case with values, offsets in the genome. And it's a multimap because a k-mer may be associated with many different offsets in the genome.
    
    - ##### [SubSequence Indexing](https://github.com/visheshsinha/DNA_Sequencing/blob/master/subseq_index.py):
    > In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
            
            
    
#### Need for Approximate Matching Algorithms :

- We need algorithms that can do approximate matching. Allowing for differences between the pattern and the text. One of the reason we might expect differences between the read and the reference is because of sequencing errors. Sometimes the sequencer will make mistakes. It will miscall a base in the sequencing read. And when that happens, that base might no longer match the reference genome.

- We want to be able to talk about the distance between two strings. In other words, we want to be able to describe how different they are, how many differences there are. But we have to define exactly what we mean by distance. 
  - So the first kind of distance we'll define is called [_Hamming Distance_](https://github.com/visheshsinha/DNA_Sequencing/blob/master/hammingDistance.py). So if you have two strings, _X_ & _Y_, that are of the same length, we can define the hamming distance between X and Y as the minimal number of substitutions we need to make to turn one of the strings into the other. 
  - Another is [_Edit Distance(AKA levenshtein Distance)_](https://github.com/visheshsinha/DNA_Sequencing/blob/master/editDistance.py) between two strings equals the minimal number of edits required to turn one string into the other. Where a single edit could be a substitution, or it could be an insertion or a deletion. (In this case _X_ & _Y_ could be of different length)
  
  - [Approximate Matching Algorithm using Pigeonhole Principle (and Boyer Moore)](https://github.com/visheshsinha/DNA_Sequencing/blob/master/approximate_pigeonhole.py) : The Pigeonhole Principle states that if items are put into containers, with, then at least one container must contain more than one item. In our case we will split _pattern 'P'_ (k+1) times when we are looking for an approximate match of upto _'k'_ mismatches, that means even if we have _'k'_ mismatches in _'k'_ partitions of pattern _'P'_, still there will be atleast one partition which will exactly match with the reference genome, which we can later confirm by verification as stated in indexing techiques.
  
  - [Global Alignment](https://github.com/visheshsinha/DNA_Sequencing/blob/master/globalAlignment.py): Calculating a global alignment is a form of global optimization that "forces" the alignment to span the entire length of all query sequences. By contrast, local alignments identify regions of similarity within long sequences that are often widely divergent overall. An attempt is made to align the entire sequence (end to end alignment) Finds local regions with the highest level of similarity between the two sequences. A global alignment contains all letters from both the query and target sequences. It penalises the Substitution/ Insertion/ Deletion differently than editDistance.

  - [Overlaps](https://github.com/visheshsinha/DNA_Sequencing/blob/master/overlaps.py): Overlap–layout–consensus genome assembly algorithm: Reads are provided to the algorithm. Overlapping regions are identified. Each read is graphed as a node and the overlaps are represented as edges joining the two nodes involved. The algorithm determines the best path through the graph (Hamiltonian path).
  
  - [Shortest Common Superstring](https://github.com/visheshsinha/DNA_Sequencing/blob/master/shortestcommonsuperstring.py): A shortest common supersequence (SCS) is a common supersequence of minimal length. In the shortest common supersequence problem, two sequences X and Y are given, and the task is to find a shortest possible common supersequence of these sequences.