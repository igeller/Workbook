import string
import sys
import os
import argparse
import re

#
# fa-sim.py
#
# author: bjr
# date: 21 jan 2020
# last update: 4 feb 2020
#
#


class FiniteAutomata:

    def __init__(self):
        self.start_state = ""
        self.final_states = set()
        # transitions is a dictionary (s,q)->R
        # - s in { \w|:} where ":" is an epsilon move,
        # - R subset of Q, and for a DFA, |R|=1
        self.transitions = {}

        # the set of states the NFA, or the singleton set
        # of the state the DFA.
        # when changing this to an NFA, use set()
        self.current_state = self.start_state

    def set_start_state(self, state):
        self.start_state = state

    def add_final_state(self, state):
        self.final_states.add(state)

    def add_transition(self, state_from, symbol, state_to):
        if symbol == ":":
            print("WARNING: epsilon moves not allowed for DFA's; but will allow")
        x = (symbol, state_from)
        if x in self.transitions:
            print(self.transitions)
            print(x[0])
            print("WARNING: multiple outgoing states not allowed for DFA's; overwriting")
            self.transitions[x] = state_to
        else:
            self.transitions[x] = state_to

    def restart(self):
        self.current_state = self.start_state

    def step_transition(self, symbol):
        """
        take one state transition, based on the given symbol symbol, updating the current_state
        """
        c_s = self.current_state
        if (symbol, c_s) in self.transitions:
            s = self.transitions[(symbol, c_s)]
            self.current_state = s
            # print("on", symbol, "goto state",self.current_state)
        else:
            # print("transition" ,(symbol,self.current_state),"not found")
            assert (False)

    def epsilon_closure(self, set_of_states):
        """
        given the set, set_of_states, compute and return that set that is the epsilon closure
        """
        return set()

    def accept_string(self, word):
        self.restart()
        for b in word:
            m = re.search('(\w)', b)
            if m:
                self.step_transition(m.group(1))
        return self.current_state in self.final_states

    def print_fa(self):
        print("\nstart state:\n\t", self.start_state)
        print("final state(s):")
        for s in self.final_states:
            print("\t", s)
        print("transitions:")
        for t in self.transitions:
            print("\t", t, "->", self.transitions[t])

    def create_fa_from_description(self, fa_string):
        """
        code to parse a Finite Automata description into the FiniteAutomata object.
        this should not need to be changed when modifying the code to an NFA.
        the parsing for either kind of FA is the same, just how the parased data
        gets stored in the FiniteAutomata object.
        """

        fa_obj = FiniteAutomata()
        fa_array = fa_string.splitlines()
        line_no = 0
        current_state = ""
        in_state_read = False
        in_final_read = False

        for line in fa_array:
            while True:
                # comment lines are fully ignored
                if re.search('^\s*#', line):
                    # print(line_no, "comment:")
                    break

                if in_state_read:
                    m = re.search('\s+(\w|:)\s+(\w+)', line)
                    if m:
                        # print(line_no,"add",m.group(1),m.group(2),"to state")
                        fa_obj.add_transition(current_state, m.group(1), m.group(2))
                        break

                if in_final_read:
                    m = re.search('\s+(\w+)', line)
                    if m:
                        # print(line_no,"add",m.group(1),"as final state")
                        fa_obj.add_final_state(m.group(1))
                        break

                in_state_read = False
                in_final_read = False

                # blank lines do end multiline input
                if re.search('^\s*$', line):
                    # print(line_no, "blank line")
                    break

                m = re.search('^start:\s*(\w+)', line)
                if m:
                    # print(line_no, "start state is",m.group(1))
                    fa_obj.set_start_state(m.group(1))
                    break

                m = re.search('^final:\s*(\w+)', line)
                if m:
                    # print(line_no,"final state dcl",m.group(1))
                    fa_obj.add_final_state(m.group(1))
                    in_final_read = True
                    break

                m = re.search('^state:\s*(\w+)', line)
                if m:
                    # print(line_no,"state dcl",m.group(1))
                    in_state_read = True
                    current_state = m.group(1)
                    break

                print(line_no, "warning: unparsable line, dropping")
                break

            line_no += 1
        return fa_obj



# stuff for a run
o = FiniteAutomata();

fad = """
#
# finite automata from Sipser, figure 1.6
#
# accepts any string ending in a 1 or containing
# a 1 and ending with an even number of 0's
#

start: q1

final: q2
    r
    r


state: q1
    0 q1
    1 q2
    : q4
    1 q2

state: q2
    1 q2
    0 q3

state: q3
    0 q2
    1 q2

"""

tests = """0
1

10
100
10100
"""

def fa_do(fad, tests):
    fa_obj = o.create_fa_from_description(fad)
    fa_obj.print_fa()

    w_array = tests.splitlines()
    for word in w_array:
        word = word.strip()
        res = fa_obj.accept_string(word)
        if len(word) == 0:
            word = ":"
        print(word, "\t", res)

fa_do(fad, tests)

