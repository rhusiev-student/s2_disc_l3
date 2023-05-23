"""Generic automaton module."""
from __future__ import annotations


class State:
    """A state in an automaton.

    Attributes:
        name (str): The name of the state.
        transitions (dict[str, str]): A dictionary of transitions in the form of
            {input: next_state}.
        random_transitions (dict[str, str]): A dictionary of random transitions in
            the form of {input: next_state}.
        description (str): A description of the state.
    """

    def __init__(self, name: str, description: str | None = None) -> None:
        self.name = name
        self.transitions: dict[str, str] = {}
        self.random_transitions: dict[str, str] = {}
        if not description:
            description = f"I'm {self.name}."

        self.description = description

    def __repr__(self) -> str:
        """Return a string representation of the state.

        Returns:
            str: A string representation of the state in the form of
            "State(name)".
        """
        return f"State({self.name})"

    def __getitem__(self, key: str) -> str:
        """Return the next state given an input.

        Args:
            key (str): The input.

        Returns:
            str: The next state.
        """
        return self.transitions[key]


class Automaton:
    """The automaton with states and transitions between them.

    Attributes:
        states (dict[str, State]): A dictionary of states in the form of {name: state}.
        current_state (State): The current state.
    """

    def __init__(self) -> None:
        self.states: dict[str, State] = {}
        self.current_state: State

    def set_state(self, state: State) -> None:
        """Set the current state.

        Args:
            state (State): The state to set.
        """
        self.current_state = state

    def add_state(self, state: State) -> None:
        """Add a state to the automaton.

        Args:
            state (State): The state to add.
        """
        self.states[state.name] = state

    def add_transition(
        self, state_name: str, input_str: str, next_state_name: str
    ) -> None:
        """Add a transition to the automaton.

        Args:
            state_name (str): The name of the state to transition from.
            input_str (str): The input to transition on.
            next_state_name (str): The name of the state to transition to.
        """
        self.states[state_name].transitions[input_str] = next_state_name

    def send(self, input: str | list[str]) -> None:
        """Send an input to the automaton.

        It can be a single input or a string of inputs.

        Args:
            input (str | list[str]): The input(s) to send.
        """
        if isinstance(input, str):
            input = [input]

        for i in input:
            self.current_state = self.states[self.current_state[i]]

    def __repr__(self) -> str:
        """Return a string representation of the automaton.

        Returns:
            str: A string representation of the automaton in the form of
            "Automaton(states, current_state)".
        """
        return f"Automaton({self.states}, {self.current_state})"
