import httpx

from urllib.parse import quote


class Resource:
    async def _get(self, url: str, params: dict = None) -> dict:
        async with httpx.AsyncClient(base_url=self.BASE_URL) as client:
            req = await client.get(url, params=params)
        return req.json()


class OccurrenceResource(Resource):
    BASE_URL = "https://biocache-ws.ala.org.au"

    async def search(self, q: str, **params):
        """
        JSON occurrence search. In addition to the parameters listed,
        range based faceting is supported by using the SOLR parameters.

        The facets, q and fq values support the stored & indexed fields

        For Example (formatted for readability):

        /occurrences/search?q=AdjustedSeedQuantity_i:[* TO *]
        &pageSize=0&facets=uncertainty &facet.range=ViabilitySummary_d
        &f.ViabilitySummary_d.facet.range.start=20.0
        &f.ViabilitySummary_d.facet.range.end=100.0
        &f.ViabilitySummary_d.facet.range.gap=10 &facet.range=AdjustedSeedQuantity_i
        &f.AdjustedSeedQuantity_i.facet.range.start=0
        &f.AdjustedSeedQuantity_i.facet.range.end=100000
        &f.AdjustedSeedQuantity_i.facet.range.gap=50000

        q * String
        Query of the form field:value
        e.g. q=genus:Macropus or a free text search e.g. q=Macropus

        fq  String
        Filters to be applied to the original query.
        These are additional params of the form fq=INDEXEDFIELD:VALUE
        e.g. fq=kingdom:Fungi.
        See http://biocache.ala.org.au/ws/index/fields for all the fields that a queryable.

        facet   String
        Supported values are "off" or "on". By default, its "on".
        This is worth switching off if facetting is not required, to reduce the JSON being sent.

        facets  String
        Comma separated list of the fields to create facets on e.g. facets=basis_of_record.

        pageSize    Integer
        Number of records to return

        startIndex  Integer
        Record offset, to enable paging

        sort    String
        The indexed field to sort by

        dir String
        Supports "asc" or "desc"

        flimit  Integer
        Maximum number of facet values to return

        fsort   String
        Method in which to sort the facets either "count" or "index"

        foffset Integer
        Facet offset, to enable paging

        fprefix String
        Limits facets to values that start with the supplied value

        lat Double
        The decimal latitude to limit records to.
        Use with lon and radius to specify a "search" circle

        lon Double
        The decimal latitude to limit records to.
        Use with lon and radius to specify a "search" circle

        radius  Double
        The radius in which to limit records (relative to the lat, lon point).
        Use with lat and lon to specify a "search" circle.

        wkt String
        The polygon area in which to limit records.
        For information on Well known text see this

        Examples
        Peter Neish's D3 mashup
        A very nice D3 mashup produced by Peter Neish.

        Blog article here:
        http://peter.neish.net/using-d3js-to-visualise-the-atlas-of-living-australia/

        URL: https://biocache-ws.ala.org.au/ws/occurrences/search
        Online demo: http://peterneish.github.io/d3/ala/
        Search for the records for the genus Macropus
        Search for the records for the genus Macropus returning taxonomic, geospatial, temporal information for occurrences.

        URL: https://biocache-ws.ala.org.au/ws/occurrences/search?q=genus:Macropus
        History

        Find species of Macropus that have an invalid
        An example of using assertions to filter taxa

        URL: https://biocache-ws.ala.org.au/ws/occurrences/search?q=genus:Macropus&pageSize=0&fq=assertions:invalidCollectionDate
        History
        """

        req_params = {k: v for k, v in params.items() if v}
        req_params["q"] = quote(q)
        res = await self._get(f"ws/occurrences/search", params=req_params)
        return res


class SpeciesResource:

    BASE_URL = "https://bie-ws.ala.org.au"

    async def _get(self, url: str, params: dict = None) -> dict:
        async with httpx.AsyncClient(base_url=self.BASE_URL) as client:
            req = await client.get(url, params=params)
        return req.json()

    # async def lookup_with_guid(self, guid: str) -> dict:
    #     """
    #     Species lookup with GUID - https://bie-ws.ala.org.au/ws/species/{guid}.json

    #     guid    String
    #     The guid for the taxon concept

    #     """
    #     res = await self._get(f"/ws/species/{guid}")
    #     return res

    async def search(self, q: str, **params) -> dict:
        """
        Species free text search services.

        Example URL:
        http://bie.ala.org.au/ws/search.json?q=fish&facets=idxtype,rank,speciesGroup,imageAvailable

        q   String
        Query of the form field:value e.g. q=rk_genus:Macropus or a free text search
        e.g. q=Macropus

        fq  String
        Filters to be applied to the original query.
        These are additional params of the form fq=INDEXEDFIELD:VALUE
        e.g. fq=rank:kingdom.
        See http://bie.ala.org.au/ws/indexFields for all the fields that a queryable.

        start   Integer
        Record offset, to enable paging

        pageSize    Integer
        Number of records to return

        sort    String
        Field to sort on

        dir String
        Sort direction "asc" or "desc"

        facets  String
        Comma separated list of fields to display facets for.
        Available fields listed http://bie.ala.org.au/ws/indexFields.
        """

        req_params = {k: v for k, v in params.items() if v}
        req_params["q"] = quote(q)
        res = await self._get("/ws/search.json", params=req_params)
        return res
