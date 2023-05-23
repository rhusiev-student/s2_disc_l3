"""My day represented using automaton."""
from automaton import Automaton, State


class Day(Automaton):
    """A day represented using automaton.

    Attributes:
        states (dict[str, State]): A dictionary of states in the form of {name: state}.
        current_state (State): The current state.
        hour (int): The current hour of the day.
    """

    def __init__(self, initial_state: State = State("sleeping")) -> None:
        """Initialize MyLife.

        Args:
            initial_state (State, optional): The initial state.
                Defaults to State("sleeping").
        """
        super().__init__()
        self.add_state(initial_state)
        self.set_state(initial_state)
        self.hour = 6

    def __str__(self) -> str:
        """Return a string representation of the current state of the day.

        Returns:
            str: A string representation of the current state of the day.
        """
        transitions = "\n    ".join(
            f"'{transition}' - '{self.current_state[transition]}'"
            for transition in self.current_state.transitions.keys()
        )
        transitions += "\n    None - 'next hour'"
        return f"""It's {self.hour} o'clock.
I'm {self.current_state.name}.

Possible transitions:
{transitions}
"""

    def next_hour(self, transition: str | None = None) -> None:
        """Move to the next hour of the day.

        Args:
            transition (str, optional): The transition to take.
                Defaults to None.
        """
        if transition is not None:
            self.set_state(self.states[self.current_state[transition]])

        self.set_state(self.states[self.current_state["next hour"]])
        self.hour += 1

    def start_day(self) -> None:
        """Start the day.

        Start the loop of 24 hours. For each hour ask the user for an event. If none is
        given, just go to the next hour.
        """
        while self.hour < 24:
            print(self)
            self.next_hour(input("What to do: "))

        print("I'm going to sleep. The next day will be better.")
