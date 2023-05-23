"""My day in a form of an automaton."""
from day import Day, DayState


class MyDay(Day):
    """My day in a form of an automaton."""

    def __init__(self) -> None:
        """Initialize the automaton."""
        self.states = {}
        self.hour = 6
        self.add_my_states()
        self.add_my_transitions()

    def add_my_states(self) -> None:
        """Add my day states."""
        sleep_state = DayState("sleeping", 0)
        self.add_state(sleep_state)
        self.set_state(sleep_state)
        self.add_state(DayState("oversleeping"))
        self.add_state(DayState("overoversleeping"))
        self.add_state(DayState("overoveroversleeping"))
        self.add_state(DayState("overoveroveroversleeping"))
        self.add_state(DayState("day_ruined", 24, "My day is ruined."))
        self.add_state(DayState("reading_news", 1, "I'm reading news."))
        self.add_state(DayState("eating_breakfast", 1, "I'm eating breakfast."))
        self.add_state(DayState("eating_lunch", 1, "I'm eating lunch."))
        self.add_state(DayState("eating_lunch_after_queue", 1, "I'm eating lunch."))
        self.add_state(DayState("eating_dinner", 1, "I'm eating dinner."))
        self.add_state(
            DayState("eating_dinner_after_side_project", 1, "I'm eating dinner.")
        )
        self.add_state(DayState("studying", 4))
        self.add_state(DayState("studying_hungry", 0, "I'm studying hungry."))
        self.add_state(DayState("studying_after_being_hungry", 3, "I'm studying."))
        self.add_state(DayState("studying_after_dinner", 2, "I'm studying."))
        self.add_state(DayState("playing_games", 2, "I'm playing games."))
        self.add_state(DayState("watching_youtube", 2, "I'm watching YouTube."))
        self.add_state(DayState("walking_to_class", 1, "I'm walking to class."))
        self.add_state(DayState("walking_from_class", 1, "I'm walking from class."))
        self.add_state(
            DayState(
                "walking_from_class_after_side_project", 1, "I'm walking from class."
            )
        )
        self.add_state(DayState("commuting", 0))
        self.add_state(DayState("having_class", 4, "I'm having class."))
        self.add_state(DayState("doing_side_project", 0, "I'm doing a side project."))

    def add_my_transitions(self) -> None:
        """Add my day transitions."""
        self.add_transition("sleeping", "alarm", "reading_news")
        self.add_transition("sleeping", "next", "oversleeping")
        self.add_random_transition("sleeping", "next", "oversleeping")
        self.add_transition("oversleeping", "wake_up", "day_ruined")
        self.add_transition("oversleeping", "next", "overoversleeping")
        self.add_random_transition("oversleeping", "next", "overoversleeping")
        self.add_transition("overoversleeping", "wake_up", "day_ruined")
        self.add_transition("overoversleeping", "next", "overoveroversleeping")
        self.add_random_transition("overoversleeping", "next", "overoveroversleeping")
        self.add_transition("overoveroversleeping", "wake_up", "day_ruined")
        self.add_transition("overoveroversleeping", "next", "overoveroveroversleeping")
        self.add_random_transition(
            "overoveroversleeping", "next", "overoveroveroversleeping"
        )
        self.add_transition("overoveroveroversleeping", "wake_up", "day_ruined")
        self.add_transition("overoveroveroversleeping", "next", "day_ruined")
        self.add_random_transition("overoveroveroversleeping", "next", "day_ruined")
        self.add_transition("reading_news", "next", "eating_breakfast")

        self.add_transition("eating_breakfast", "next", "walking_to_class")
        self.add_transition("walking_to_class", "next", "having_class")
        self.add_random_transition("walking_to_class", "no_time", "commuting")
        self.add_transition("commuting", "next", "having_class")
        self.add_random_transition("commuting", "no_bus", "day_ruined")

        self.add_transition("having_class", "next", "eating_lunch")
        self.add_transition("eating_lunch", "next", "studying")
        self.add_random_transition("eating_lunch", "long_queue", "studying_hungry")
        self.add_transition("studying_hungry", "next", "eating_lunch_after_queue")
        self.add_transition(
            "eating_lunch_after_queue", "next", "studying_after_being_hungry"
        )

        self.add_transition("studying", "next", "walking_from_class")
        self.add_random_transition("studying", "too_much_homework", "day_ruined")
        self.add_transition("studying_after_being_hungry", "next", "walking_from_class")
        self.add_random_transition(
            "studying_after_being_hungry", "too_much_homework", "day_ruined"
        )
        self.add_random_transition(
            "studying", "sudden_desire_for_side_project", "doing_side_project"
        )
        self.add_transition(
            "doing_side_project", "next", "walking_from_class_after_side_project"
        )

        self.add_transition("walking_from_class", "next", "eating_dinner")
        self.add_transition(
            "walking_from_class_after_side_project",
            "next",
            "eating_dinner_after_side_project",
        )

        self.add_transition("eating_dinner", "next", "watching_youtube")
        self.add_random_transition("eating_dinner", "friend_invites", "playing_games")
        self.add_transition(
            "eating_dinner_after_side_project", "next", "studying_after_dinner"
        )
        self.add_transition("studying_after_dinner", "next", "sleeping")
        self.add_transition("watching_youtube", "next", "sleeping")
        self.add_transition("playing_games", "next", "sleeping")

        self.add_transition("day_ruined", "next", "sleeping")
