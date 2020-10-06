import json
import xmltodict


class DataAdapterFactory:
    def __init__(self, raw_data):
        self.raw_data = raw_data

        if self.raw_data.startswith("<"):
            self.__class__ = XMLDataAdapter
        elif self.raw_data.startswith("{"):
            self.__class__ = JSONDataAdapter


class DataAdapter:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def as_dict(self):
        raise NotImplementedError


class JSONDataAdapter(DataAdapter):
    def as_dict(self):
        try:
            return {
                "channel": self.__parse_channel(),
                "switch": self.__parse_switch(),
                "average": self.__parse_average(),
                "majority": self.__parse_majority()
            }
        except Exception:
            print("Warning: Skipping: {}(probably not a valid JSON)".format(self.raw_data))

    def __parse_raw_data(self):
        return json.loads(self.raw_data)

    def __parse_channel(self):
        return int(self.__parse_raw_data().get("channel"))

    def __parse_switch(self):
        return self.__parse_raw_data().get("switch")

    def __parse_average(self):
        return int(self.__parse_raw_data().get("average"))

    def __parse_majority(self):
        return self.__parse_raw_data().get("majority")


class XMLDataAdapter(DataAdapter):

    def __parse_raw_data(self):
        return json.loads(json.dumps(xmltodict.parse(self.raw_data)))["root"]

    def __parse_channel(self):
        return int(self.__parse_raw_data()["channel"]["#text"])

    def __parse_switch(self):
        return self.__parse_raw_data()["switch"]["#text"]

    def __parse_average(self):
        return int(self.__parse_raw_data()["average"]["#text"])

    def __parse_majority(self):
        return self.__parse_raw_data()["majority"]["#text"]

    def as_dict(self):
        return {"channel": self.__parse_channel(),
                "switch": self.__parse_switch(),
                "average": self.__parse_average(),
                "majority": self.__parse_majority()}
