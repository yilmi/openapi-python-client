from dataclasses import asdict
from typing import Dict, List, Optional, Union

import httpx

from ..client import AuthenticatedClient, Client
from .errors import ApiResponseError

from ..models.ping_response import PingResponse


def ping_ping_get(
    *,
    client: Client,
) -> Union[
    PingResponse,
]:
    """ A quick check to see if the system is running  """
    url = f"{client.base_url}/ping"


    response = httpx.get(
        url=url,
        headers=client.get_headers(),
    )

    if response.status_code == 200:
        return PingResponse.from_dict(response.json())
    else:
        raise ApiResponseError(response=response)