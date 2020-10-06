from collections import defaultdict, Counter
from channel_data import ChannelData
from data_adapters import DataAdapterFactory


class CodeChallengeImplementation:
    """
    Insert the logic for the coding challenge, so that main function in main.py runs without errors.
    """

    def __init__(self):
        self._channel_state = defaultdict(ChannelData)
        self._switch_state = {
            "first_switch_value": None,
            "last_switch_value": None
        }

    def set_channel_state(self, channel, payload, *args, **kwargs):
        self._channel_state[channel].update(**payload)

    def set_switch_state(self, switch_value):
        if not self._switch_state["first_switch_value"]:
            self._switch_state["first_switch_value"] = switch_value
        self._switch_state["last_switch_value"] = switch_value

    def get_switch_state(self, reverse):
        return self._switch_state["first_switch_value"] if reverse else self._switch_state["last_switch_value"]

    def get_state_average(self, reverse):
        return sum([i.get_average(reverse) for i in self._channel_state.values()]) / len(self._channel_state.values())

    def get_state_majority(self, reverse):
        return Counter([v.get_majority(reverse) for _, v in self._channel_state.items()]).most_common()[0][0]

    def merge(self, content) -> None:
        channel, payload = self.__handle_incoming_data(content)
        if channel and payload:
            self.set_channel_state(channel, payload)
            self.set_switch_state(payload["switch"])

    def state(self) -> dict:
        """ Return the current merged state. """
        return self.__state_builder()

    def reversed_state(self) -> dict:
        """ Return the state if the messages were received in the reversed order. """
        return self.__state_builder(reverse=True)

    @staticmethod
    def __handle_incoming_data(content):
        try:
            incoming_data = DataAdapterFactory(content).as_dict()
            incoming_channel = incoming_data.pop('channel')
            return incoming_channel, incoming_data
        except Exception:
            return None, None

    def __state_builder(self, reverse=False):
        return {
            "switch": self.get_switch_state(reverse),
            "average": self.get_state_average(reverse),
            "majority": self.get_state_majority(reverse)
        }
