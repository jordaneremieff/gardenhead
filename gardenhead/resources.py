import httpx

from urllib.parse import quote


class SpeciesResource:

    BASE_URL = "https://bie-ws.ala.org.au"

    async def _get(self, url: str, params: dict = None) -> dict:
        async with httpx.AsyncClient(base_url=self.BASE_URL) as client:
            req = await client.get(url, params=params)
        return req.json()

    async def lookup_with_guid(self, guid: str) -> dict:
        """
        Species lookup with GUID - https://bie-ws.ala.org.au/ws/species/{guid}.json

        guid    String
        The guid for the taxon concept

        """
        res = await self._get(f"/ws/species/{guid}")
        return res

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
