#!/usr/bin/env python

from entities.colors import TrafficLightColor
import random

class Stoplight:
    """
    Represents the stoplight in the simulation.

    Attributes:
    - color_NS: color of the north-south direction
    - color_EW: color of the east-west direction
    - time_yellow: time that the stoplight has been yellow
    - time_green: time that the stoplight has been green

    Constants:
    - YELLOW_DURATION: duration of the yellow light in ticks
    """
    YELLOW_DURATION = 90  # ticks

    def __init__(self):
        # generate random color for north-south direction:
        self.color_NS = TrafficLightColor.GREEN.value if random.choice([True, False]) else TrafficLightColor.RED.value
        # set the opposite color for east-west direction:
        self.color_EW = TrafficLightColor.RED.value if self.color_NS == TrafficLightColor.GREEN.value else TrafficLightColor.GREEN.value

        self.time_yellow = 0
        self.time_green = 0

    def get_ns_color(self):
        return self.color_NS
    
    def get_ew_color(self):
        return self.color_EW

    def switch_yellow(self):
        """
        Switch the stoplight that is green to yellow.
        """
        if self.color_NS == TrafficLightColor.GREEN.value:
            self.color_NS = TrafficLightColor.YELLOW.value
            self.time_green = 0
        elif self.color_EW == TrafficLightColor.GREEN.value:
            self.color_EW = TrafficLightColor.YELLOW.value
            self.time_green = 0

    def update_stoplight(self):
        """
        Update the time that the stoplight has been green and/or yellow.

        Update the color of the yellow stoplight when the yellow light duration is reached.
        """
        if self.color_NS == TrafficLightColor.GREEN.value or self.color_EW == TrafficLightColor.GREEN.value:
            self.time_green += 1
        if self.color_NS == TrafficLightColor.YELLOW.value or self.color_EW == TrafficLightColor.YELLOW.value:
            self.time_yellow += 1

        if self.time_yellow >= Stoplight.YELLOW_DURATION:
            if self.color_NS == TrafficLightColor.YELLOW.value:
                self.color_NS = TrafficLightColor.RED.value
                self.color_EW = TrafficLightColor.GREEN.value
            elif self.color_EW == TrafficLightColor.YELLOW.value:
                self.color_EW = TrafficLightColor.RED.value
                self.color_NS = TrafficLightColor.GREEN.value
            self.time_yellow = 0