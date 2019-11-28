# Foward Planning Agent

## Introduction
This project is split between implementation and analysis. I combined symbolic logic and classical search to implement an agent that performs progression search to solve planning problems. Then I experimented with different search algorithms and heuristics, and use the results to answer questions about designing planning systems.


## Run
Experiment with different search algorithms using the `run_search.py` script. (See example usage below.) The goal of the experiment is to understand the tradeoffs in speed, optimality, and complexity of progression search as problem size increases. You will record your results in a report (described below in Report Requirements).

Run the search experiment manually (you will be prompted to select problems & search algorithms)

``
$ python run_search.py -m
``

You can also run specific problems & search algorithms - e.g., to run breadth first search and UCS on problems 1 and 2:

``
$ python run_search.py -p 1 2 -s 1 2
``
