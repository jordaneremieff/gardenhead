from gardenhead.resources import SpeciesResource


def test_species_resource_search() -> None:
    resource = SpeciesResource()
    res = resource.search("grevillea")
    print(res)
