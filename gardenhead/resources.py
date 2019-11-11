import httpx

from urllib.parse import quote


class SpeciesResource:

    BASE_URL = "https://bie-ws.ala.org.au/ws/"

    def search(self, q: str, **params) -> dict:
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

        req_params = {k: v for k, v in params if v}
        req_params["q"] = quote(q)

        url = f"{self.BASE_URL}/search.json"
        req = httpx.get(url, params=req_params)
        return req.json()
