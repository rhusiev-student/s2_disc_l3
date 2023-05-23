"""My day represented using automaton."""
from automaton import Automaton, State


class DayState(State):
    """A state of the day.

    Attributes:
        name (str): The name of the state.
        transitions (dict[str, str]): A dictionary of transitions in the form of
        skip_hour (int): The number of hours to skip.
    """

    def __init__(self, name: str, skip_hour: int = 1) -> None:
        super().__init__(name)
        self.skip_hour = skip_hour


class Day(Automaton):
    """A day represented using automaton.

    Attributes:
        states (dict[str, DayState]): A dictionary of states in the form of
            {name: state}.
        current_state (DayState): The current state.
        hour (int): The current hour of the day.
    """

    def __init__(self, initial_state: DayState = DayState("sleeping")) -> None:
        """Initialize MyLife.

        Args:
            initial_state (DayState, optional): The initial state.
                Defaults to DayState("sleeping").
        """
        self.states = {}
        self.current_state: DayState
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
        transitions += "\n    None <=> 'next'"
        return f"""It's {self.hour} o'clock.
I'm {self.current_state.name}.

Possible transitions:
    {transitions}
"""

    def next_hour(self, transition: str) -> None:
        """Move to the next hour of the day.

        Args:
            transition (str): The transition to take.
                Defaults to None.
        """
        self.hour += self.current_state.skip_hour
        if transition:
            if transition not in self.current_state.transitions:
                print("There is no such transition.")
                return

            self.set_state(self.states[self.current_state[transition]])
        else:
            self.set_state(self.states[self.current_state["next"]])

        if self.hour >= 22:
            self.end_of_day = True

    def start_day(self) -> None:
        """Start the day.

        Start the loop of 24 hours. For each hour ask the user for an event. If none is
        given, just go to the next hour.
        """
        self.end_of_day = False
        while not self.end_of_day:
            print(self)
            self.next_hour(input("What to do: "))

        print("It's 22 o'clock. I'm going to sleep.")
        print("The next day will be better.")
