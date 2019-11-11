from dataclasses import dataclass


@dataclass
class Species:

    data: dict

    @property
    def scientific_name(self):
        return self.data.get("scientificName")

    @property
    def thumbnail_url(self):
        return self.data.get("thumbnailUrl")

    @property
    def name_formatted(self):
        return self.data.get("nameFormatted")

    @property
    def kingdom(self):
        return self.data.get("kingdom")

    @property
    def genus(self):
        return self.data.get("genus")
