# -*- coding: utf-8 -*-  # noqa

from intercom import lead
from intercom.api_operations.all import All
from intercom.api_operations.convert import Convert
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.delete import Delete
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class Lead(BaseService, All, Find, FindAll, Delete, Save, Load, Convert):
    """Leads are useful for representing logged-out users of your application.

    Ref: https://developers.intercom.io/reference#leads
    """

    @property
    def collection(self):
        """Return the name of the collection."""
        return utils.resource_class_to_collection_name(self.collection_class)

    @property
    def collection_class(self):
        """The collection class that represents this resource."""
        return lead.Lead

    def convert(self, _id, _email):
        """convert a lead to a user"""
        service_url = "/contacts/convert/%s" % _id #different service_url for conversion
        data = {
            'contact': {
                'user_id' : _id,
             },
            'user': {
                'email' : _email,
            }
        }
        response = self.client.post(service_url, data)
        return self.collection_class().from_response(response)


