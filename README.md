_Note : All the Rendered Juypter Notebooks(in nbviewer) for better view are availabe by clicking on the links embedded below._
### [DNA Sequencing](https://nbviewer.jupyter.org/github/visheshsinha/DNA_Sequencing/blob/master/DNA_Sequencing.ipynb) 

![N|Solid](https://cdn.technologynetworks.com/tn/images/thumbs/webp/640_360/rapid-sars-cov-2-genome-sequencing-to-support-outbreak-investigations-334486.webp?v=10702522)

#### Read Alignment Algorithms Covered : 
- #### Online Algorithms: 
    The algorithm in which the text 'T' (in our case the reference genome) is not pre-processed, and it doesn't matter if the pattern 'P' is pre-processed or not.
    - ##### [Naive Exact Matching Algorithm](https://github.com/visheshsinha/DNA_Sequencing/blob/master/naive_algo.py) : 
         >We niether pre-process 'P' nor 'T'.
    - ##### [Boyer-Moore (using Z-Algorithm)](https://nbviewer.jupyter.org/github/visheshsinha/DNA_Sequencing/blob/master/Boyer's_Moore_Pattern_Matching.ipynb) :
         >Here we pre-process 'P' but not 'T' so it's online.
        
        - ##### Text Resource : Go Through Chapter 2 of [Algorithms on Strings, Trees, and Sequences( by Dan Gusfield)](https://doi.org/10.1017/CBO9780511574931)
        - ##### Video Resource : Linear-time pattern matching : Z-values and Z-algorithm ( by Dan Gusfield) [Part 1](https://youtu.be/MFK0WYeVEag) [Part 2](https://youtu.be/NVJ_ELSbbew)

- #### Offline Algorithms: 
    The algorithm in which the text 'T' is  pre-processed, and it doesn't matter if the pattern 'P' is pre-processed or not.

    - ##### [Indexing and the k-mer index](https://nbviewer.jupyter.org/github/visheshsinha/DNA_Sequencing/blob/master/Indexing_K-mer.ipynb) : 
    
    >We use the term k-mer to refer to a substring of length k. For each offset that the index reports back, that's called an index hit. When P matches within T, we've been calling that a match, or an occurrence. But, an index hit may or may not correspond to a match, it's just a hint that we should look harder in that particular region of T. So, not all index hits lead to matches, because we don't know whether the rest of P matches where it should within T. We have to do more character comparisons. And, this additional work that we do is called verification.
    >
    >This kind of data structure is called a multimap. It's a map because it associates keys, k-mers, in this case with values, offsets in the genome. And it's a multimap because a k-mer may be associated with many different offsets in the genome.