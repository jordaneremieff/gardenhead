import pytest

from gardenhead.resources import SpeciesResource, OccurrenceResource


@pytest.mark.asyncio
async def test_species_resource_search(server) -> None:
    resource = SpeciesResource()
    resource.BASE_URL = "http://127.0.0.1:8000"
    records = await resource.search("grevillea", pageSize=1)
    # print(records)


@pytest.mark.asyncio
async def test_occurrence_resource_search(server) -> None:
    resource = OccurrenceResource()
    resource.BASE_URL = "http://127.0.0.1:8000"
    records = await resource.search("grevillea", pageSize=1)
    # print(records)


# @pytest.mark.asyncio
# async def test_species_resource_lookup_with_guid(server) -> None:
#     resource = SpeciesResource()
#     # resource.BASE_URL = "http://127.0.0.1:8000"
#     record = await resource.lookup_with_guid(
#         "http://id.biodiversity.org.au/node/apni/9493859.json"
#     )
#     print(record)
