# coding: utf-8

"""
    Hatchet API

    The Hatchet API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hatchet_sdk.clients.rest.models.api_resource_meta import APIResourceMeta
from hatchet_sdk.clients.rest.models.event import Event
from typing import Optional, Set
from typing_extensions import Self

class WorkflowRunTriggeredBy(BaseModel):
    """
    WorkflowRunTriggeredBy
    """ # noqa: E501
    metadata: APIResourceMeta
    parent_id: StrictStr = Field(alias="parentId")
    event_id: Optional[StrictStr] = Field(default=None, alias="eventId")
    event: Optional[Event] = None
    cron_parent_id: Optional[StrictStr] = Field(default=None, alias="cronParentId")
    cron_schedule: Optional[StrictStr] = Field(default=None, alias="cronSchedule")
    __properties: ClassVar[List[str]] = ["metadata", "parentId", "eventId", "event", "cronParentId", "cronSchedule"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorkflowRunTriggeredBy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkflowRunTriggeredBy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": APIResourceMeta.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "parentId": obj.get("parentId"),
            "eventId": obj.get("eventId"),
            "event": Event.from_dict(obj["event"]) if obj.get("event") is not None else None,
            "cronParentId": obj.get("cronParentId"),
            "cronSchedule": obj.get("cronSchedule")
        })
        return _obj


