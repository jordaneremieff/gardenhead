import httpx

from gardenhead.resources import SpeciesResource


def test_species_resource_search() -> None:
    resource = SpeciesResource()
    res = resource.search("grevillea", pageSize=1)
    # print(res)


def test_species_resource_lookup_with_guid() -> None:
    resource = SpeciesResource()
    res = resource.lookup_with_guid(
        "http://id.biodiversity.org.au/node/apni/9493859.json"
    )
    print(res)
