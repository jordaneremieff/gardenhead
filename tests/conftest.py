import pytest
import time
import threading

from uvicorn.config import Config
from uvicorn.main import Server
from starlette.applications import Starlette
from starlette.responses import JSONResponse


app = Starlette()


@app.route("/ws/search.json")
def mock_species_search(request):
    q = request.query_params.get("q")
    mock_result = {
        "searchResults": {
            "totalRecords": 2190,
            "facetResults": [],
            "results": [
                {
                    "id": "f8a622fc-e5c7-4aa8-92c7-c4ea80a84254",
                    "guid": "http://id.biodiversity.org.au/node/apni/9493859",
                    "linkIdentifier": "Grevillea",
                    "idxtype": "TAXON",
                    "name": "Grevillea",
                    "kingdom": "Plantae",
                    "nomenclaturalCode": "ICBN",
                    "scientificName": "Grevillea",
                    "scientificNameAuthorship": "R.Br. ex Knight",
                    "author": "R.Br. ex Knight",
                    "nameComplete": "Grevillea R.Br. ex Knight",
                    "nameFormatted": '<span class="scientific-name rank-genus"><span class="name">Grevillea</span> <span class="author ex-author">R.Br.</span> ex <span class="author">Knight</span></span>',
                    "taxonomicStatus": "accepted",
                    "nomenclaturalStatus": None,
                    "parentGuid": "http://id.biodiversity.org.au/node/apni/9877231",
                    "rank": "genus",
                    "rankID": 6000,
                    "commonName": "",
                    "commonNameSingle": "",
                    "occurrenceCount": 131149,
                    "conservationStatus": None,
                    "favourite": None,
                    "infoSourceName": "APC",
                    "infoSourceURL": "https://collections.ala.org.au/public/show/dr5214",
                    "image": "800f2265-f2e1-4bf7-9702-3d7c8b9d7978",
                    "imageUrl": "https://images.ala.org.au/image/proxyImageThumbnailLarge?imageId=800f2265-f2e1-4bf7-9702-3d7c8b9d7978",
                    "thumbnailUrl": "https://images.ala.org.au/image/proxyImageThumbnail?imageId=800f2265-f2e1-4bf7-9702-3d7c8b9d7978",
                    "smallImageUrl": "https://images.ala.org.au/image/proxyImageThumbnailLarge?imageId=800f2265-f2e1-4bf7-9702-3d7c8b9d7978",
                    "largeImageUrl": "https://images.ala.org.au/image/proxyImage?imageId=800f2265-f2e1-4bf7-9702-3d7c8b9d7978",
                    "kingdomGuid": "http://id.biodiversity.org.au/node/apni/50587232",
                    "phylum": "Charophyta",
                    "phylumGuid": "http://id.biodiversity.org.au/node/apni/50587231",
                    "class": "Equisetopsida",
                    "classGuid": "http://id.biodiversity.org.au/node/apni/50587230",
                    "subclass": "Magnoliidae",
                    "subclassGuid": "http://id.biodiversity.org.au/node/apni/50587229",
                    "superorder": "Proteanae",
                    "superorderGuid": "http://id.biodiversity.org.au/node/apni/9877233",
                    "order": "Proteales",
                    "orderGuid": "http://id.biodiversity.org.au/node/apni/9877232",
                    "family": "Proteaceae",
                    "familyGuid": "http://id.biodiversity.org.au/node/apni/9877231",
                    "genus": "Grevillea",
                    "genusGuid": "http://id.biodiversity.org.au/node/apni/9493859",
                }
            ],
            "queryTitle": q,
        }
    }
    return JSONResponse(mock_result)


@app.route("/ws/occurrences/search")
def mock_occurrence_search(request):
    mock_result = {
        "pageSize": 1,
        "startIndex": 0,
        "totalRecords": 131166,
        "sort": "score",
        "dir": "asc",
        "status": "OK",
        "occurrences": [
            {
                "uuid": "bc32b913-e43c-47df-a8a8-d19424da1626",
                "occurrenceID": "NSW:NSW:NSW 782740",
                "dataHubUid": ["dh2", "dh9"],
                "institutionUid": "in50",
                "raw_institutionCode": "NSW",
                "institutionName": "The Royal Botanic Gardens & Domain Trust",
                "collectionUid": "co54",
                "raw_collectionCode": "NSW",
                "collectionName": "National Herbarium of New South Wales",
                "raw_catalogNumber": "NSW 782740",
                "taxonConceptID": "http://id.biodiversity.org.au/node/apni/2919713",
                "eventDate": 528804000000,
                "occurrenceYear": 504921600000,
                "scientificName": "Grevillea acuaria",
                "taxonRank": "species",
                "taxonRankID": 7000,
                "country": "Australia",
                "kingdom": "Plantae",
                "phylum": "Charophyta",
                "classs": "Equisetopsida",
                "order": "Proteales",
                "family": "Proteaceae",
                "genus": "Grevillea",
                "genusGuid": "http://id.biodiversity.org.au/node/apni/9493859",
                "species": "Grevillea acuaria",
                "speciesGuid": "http://id.biodiversity.org.au/node/apni/2919713",
                "stateProvince": "Western Australia",
                "decimalLatitude": -32.58,
                "decimalLongitude": 119.8,
                "year": 1986,
                "month": "10",
                "basisOfRecord": "PreservedSpecimen",
                "raw_occurrenceRemarks": "Low shrub, 0.3 x 0.3 m with green linear leaves. Flowers solitary or in axillary pairs. Red perianth, 7 mm long. Green style, pistil 16 mm.  Abundant.",
                "left": 588601,
                "right": 588601,
                "lga": "Kondinin (S)",
                "dataProviderUid": "dp36",
                "dataProviderName": "Australia's Virtual Herbarium",
                "dataResourceUid": "dr376",
                "dataResourceName": "MEL AVH data",
                "assertions": ["geodeticDatumAssumedWgs84"],
                "speciesGroups": ["Plants", "Angiosperms", "Dicots"],
                "geospatialKosher": "true",
                "taxonomicKosher": "true",
                "collector": "Olde, P.M.",
                "collectors": ["Olde, P.M."],
                "raw_scientificName": "Grevillea acuaria F.Muell. ex Benth.",
                "raw_basisOfRecord": "PreservedSpecimen",
                "latLong": "-32.5800000000,119.8000000000",
                "point1": "-33,120",
                "point01": "-32.6,119.8",
                "point001": "-32.58,119.8",
                "point0001": "-32.58,119.8",
                "point00001": "-32.58,119.8",
                "namesLsid": "Grevillea acuaria|http://id.biodiversity.org.au/node/apni/2919713||Plantae|Proteaceae",
                "license": "CC-BY 3.0 (Au)",
                "recordNumber": "86/759",
            }
        ],
        "facetResults": [],
        "query": "?q=grevillea",
        "urlParameters": "?q=grevillea",
        "queryTitle": "<span class='lsid' id='http://id.biodiversity.org.au/node/apni/9493859'>GENUS: Grevillea</span>",
        "activeFacetMap": {},
    }
    return JSONResponse(mock_result)


class TestServer(Server):
    def install_signal_handlers(self):
        pass


def serve_in_thread(server: Server):
    thread = threading.Thread(target=server.run)
    thread.start()
    try:
        while not server.started:
            time.sleep(1e-3)
        yield server
    finally:
        server.should_exit = True
        thread.join()


@pytest.fixture(scope="session")
def server():
    config = Config(app=app, lifespan="off", loop="asyncio")
    server = TestServer(config=config)
    yield from serve_in_thread(server)
