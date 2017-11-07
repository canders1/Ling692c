from nltk.parse import earleychart

earleychart.demo(print_times=True, print_grammar=True, print_trees=True, trace=2, sent='I saw John with a dog with my cookie', numparses=5)