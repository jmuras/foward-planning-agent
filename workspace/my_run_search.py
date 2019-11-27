
import argparse

from aimacode.search import (breadth_first_search, astar_search,
    breadth_first_tree_search, depth_first_graph_search, uniform_cost_search,
    greedy_best_first_graph_search, depth_limited_search,
    recursive_best_first_search)
from air_cargo_problems import air_cargo_p1, air_cargo_p2, air_cargo_p3, air_cargo_p4

from _utils import run_search



PROBLEMS = [["Air Cargo Problem 1", air_cargo_p1],
            ["Air Cargo Problem 2", air_cargo_p2],
            ["Air Cargo Problem 3", air_cargo_p3],
            ["Air Cargo Problem 4", air_cargo_p4]]
SEARCHES = [["breadth_first_search", breadth_first_search, ""],
            ['depth_first_graph_search', depth_first_graph_search, ""],
            ['uniform_cost_search', uniform_cost_search, ""],
            ['greedy_best_first_graph_search', greedy_best_first_graph_search, 'h_unmet_goals'],
            ['greedy_best_first_graph_search', greedy_best_first_graph_search, 'h_pg_levelsum'],
            ['greedy_best_first_graph_search', greedy_best_first_graph_search, 'h_pg_maxlevel'],
            ['greedy_best_first_graph_search', greedy_best_first_graph_search, 'h_pg_setlevel'],
            ['astar_search', astar_search, 'h_unmet_goals'],
            ['astar_search', astar_search, 'h_pg_levelsum'],
            ['astar_search', astar_search, 'h_pg_maxlevel'],
            ['astar_search', astar_search, 'h_pg_setlevel']
            ]


if __name__=="__main__":

    p_choices = [4]
    s_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    problems = [PROBLEMS[i-1] for i in map(int, p_choices)]
    searches = [SEARCHES[i-1] for i in map(int, s_choices)]

    for pname, problem_fn in problems:
        for sname, search_fn, heuristic in searches:
            hstring = heuristic if not heuristic else " with {}".format(heuristic)
            print("\nSolving {} using {}{}...".format(pname, sname, hstring))

            problem_instance = problem_fn()
            heuristic_fn = None if not heuristic else getattr(problem_instance, heuristic)
            run_search(problem_instance, search_fn, heuristic_fn)



