"""My day in a form of an automaton."""
from day import Day, DayState


class MyDay(Day):
    """My day in a form of an automaton."""

    def __init__(self) -> None:
        """Initialize the automaton."""
        super().__init__()

    def add_my_states(self) -> None:
        """Add my day states."""
        self.add_state(DayState("sleeping"))
        self.add_state(DayState("oversleeping"))
        self.add_state(DayState("day_ruined", 24))
        self.add_state(DayState("reading_news"))
        self.add_state(DayState("eating_breakfast"))
        self.add_state(DayState("eating_lunch"))
        self.add_state(DayState("eating_lunch_after_queue"))
        self.add_state(DayState("eating_dinner"))
        self.add_state(DayState("eating_dinner_after_side_project"))
        self.add_state(DayState("studying", 4))
        self.add_state(DayState("studying_hungry", 0))
        self.add_state(DayState("studying_after_being_hungry", 3))
        self.add_state(DayState("studying_after_dinner", 2))
        self.add_state(DayState("playing_games", 2))
        self.add_state(DayState("watching_youtube", 2))
        self.add_state(DayState("walking_to_class"))
        self.add_state(DayState("walking_from_class"))
        self.add_state(DayState("walking_from_class_after_side_project"))
        self.add_state(DayState("commuting", 0))
        self.add_state(DayState("having_class", 4))
        self.add_state(DayState("doing_side_project", 0))

    def add_my_transitions(self) -> None:
        """Add my day transitions."""
        self.add_transition("sleeping", "alarm", "reading_news")
        self.add_transition("sleeping", "next_hour", "oversleeping")
        self.add_transition("oversleeping", "wake_up", "day_ruined")
        self.add_transition("reading_news", "next_hour", "eating_breakfast")

        self.add_transition("eating_breakfast", "next_hour", "walking_to_class")
        self.add_transition("walking_to_class", "next_hour", "having_class")
        self.add_transition("walking_to_class", "no_time", "commuting")
        self.add_transition("commuting", "next_hour", "having_class")
        self.add_transition("commuting", "no_bus", "day_ruined")

        self.add_transition("having_class", "next_hour", "eating_lunch")
        self.add_transition("eating_lunch", "next_hour", "studying")
        self.add_transition("eating_lunch", "long_queue", "studying_hungry")
        self.add_transition("studying_hungry", "next_hour", "eating_lunch_after_queue")
        self.add_transition(
            "eating_lunch_after_queue", "next_hour", "studying_after_being_hungry"
        )

        self.add_transition("studying", "next_hour", "walking_from_class")
        self.add_transition("studying", "too_much_homework", "day_ruined")
        self.add_transition(
            "studying_after_being_hungry", "next_hour", "walking_from_class"
        )
        self.add_transition(
            "studying_after_being_hungry", "too_much_homework", "day_ruined"
        )
        self.add_transition(
            "studying", "sudden_desire_for_side_project", "doing_side_project"
        )
        self.add_transition(
            "doing_side_project", "next_hour", "walking_from_class_after_side_project"
        )

        self.add_transition("walking_from_class", "next_hour", "eating_dinner")
        self.add_transition(
            "walking_from_class_after_side_project",
            "next_hour",
            "eating_dinner_after_side_project",
        )

        self.add_transition("eating_dinner", "next_hour", "watching_youtube")
        self.add_transition("eating_dinner", "friend_invites", "playing_games")
        self.add_transition(
            "eating_dinner_after_side_project", "next_hour", "studying_after_dinner"
        )
        self.add_transition("studying_after_dinner", "next_hour", "sleeping")
        self.add_transition("watching_youtube", "next_hour", "sleeping")
        self.add_transition("playing_games", "next_hour", "sleeping")
