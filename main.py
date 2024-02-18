from automata.fa.dfa import DFA

my_dfa = DFA(
    states={'p', 'q', 'r'},  # 'a' 'b' 'c' are auxiliary states to handle emtpy strings
    input_symbols={'0', '1', 'e'},  # 'e' represents an emtpy string
    transitions={
        'p': {'0': 'p', '1': 'q', 'e': 'p'},
        'q': {'0': 'r', '1': 'p', 'e': 'q'},
        'r': {'0': 'q', '1': 'r', 'e': 'r'}
    },
    initial_state='p',
    final_states={'p'}
)

try:
    while True:
        if my_dfa.accepts_input(input("Enter an input: ")):
            print("The automaton accepts this string")
        else:
            print("The automaton doesn't recognize this string as valid.")
except KeyboardInterrupt:
    print("")