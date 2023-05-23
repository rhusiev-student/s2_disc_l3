"""My day represented using automaton."""
from random import choice, randint

from automaton import Automaton, State


class DayState(State):
    """A state of the day.

    Attributes:
        name (str): The name of the state.
        transitions (dict[str, str]): A dictionary of transitions in the form of
        skip_hour (int): The number of hours to skip.
    """

    def __init__(
        self, name: str, skip_hour: int = 1, description: str | None = None
    ) -> None:
        super().__init__(name, description)
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
        action = (
            "I`m" + self.current_state.name + "."
            if not self.current_state.description
            else self.current_state.description
        )
        return f"""It's {self.hour} o'clock.
{action}
Possible transitions:
    {transitions}
"""

    def add_random_transition(
        self, state_name: str, input_str: str, next_state_name: str
    ) -> None:
        """Add a transition that can randomly occur to the automaton.

        Args:
            state_name (str): The name of the state to transition from.
            input_str (str): The input to transition on.
            next_state_name (str): The name of the state to transition to.
        """
        self.states[state_name].random_transitions[input_str] = next_state_name

    def next_hour(self, transition: str) -> None:
        """Move to the next hour of the day.

        Args:
            transition (str): The transition to take.
                Defaults to None.
        """
        self.hour += self.current_state.skip_hour
        if randint(0, 10) > 7 and self.current_state.random_transitions:
            transition = choice(list(self.current_state.random_transitions.keys()))
            print()
            print()
            print(f"Oops, a random event({transition}) happened!")
            print()
            self.set_state(
                self.states[self.current_state.random_transitions[transition]]
            )
            action = (
                "I`m" + self.current_state.name + "."
                if not self.current_state.description
                else self.current_state.description
            )
            print(action)

        elif transition:
            if transition not in self.current_state.transitions:
                print("There is no such transition.")
                return

            print()
            print()
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
        print(
            """It's 6 o'clock. Let's start the day!
You are given a state and possible actions(transitions) you can make from that state.
You can always just type 'next' to go to the next event without doing anything.
Sending an empty string will do the same as 'next'.
"""
        )
        self.end_of_day = False
        self.hour = 6
        self.set_state(self.states["sleeping"])

        while not self.end_of_day:
            print(self)
            self.next_hour(input("What to do: "))

        print()
        print("It's 22 o'clock. I'm going to sleep.")
        print("The next day will be better.")
        print()
        if input("Do you want to start a new day? (Y/n) ").lower() == "n":
            print("Goodbye!")
            return

        self.start_day()
